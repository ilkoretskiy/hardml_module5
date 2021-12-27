from typing import Optional
from fastapi import FastAPI
import requests
import logging
import uuid
import os
import  service_discovery as sd



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

REDIS_HOST = None
REPLICA_NAME=None
SERVICE_HOST=None
SERVICE_PORT=None

storage = {}

def retrieve_secret_value():
    unstable_source = "https://lab.karpov.courses/hardml-api/module-5/get_secret_number"
    result = requests.get(unstable_source)
    if result.status_code != 200:
        raise ValueError("wrong status code")

    value = result.json()['secret_number']
    return value

def update_secret_number():
    result = None

    max_retries = 20
    retries = 0

    while (result is None and retries < max_retries):
        print(f"Try #{retries}")
        try: 
            result = retrieve_secret_value()
        except ValueError as e:
            print(e.args)

        retries += 1

    storage['secret_number'] = result

def generate_replica_name():
    random_id =  uuid.uuid4().hex
    common_prefix = "web_app_" 
    replica_name = common_prefix + random_id
    return replica_name


def init_global_variables():
    global REPLICA_NAME, REDIS_HOST, SERVICE_HOST, SERVICE_PORT
    REPLICA_NAME = generate_replica_name()
    REDIS_HOST = os.environ["REDIS_HOST"]
    SERVICE_HOST = os.environ["SERVICE_HOST"]
    SERVICE_PORT = os.environ["SERVICE_PORT"]

def register_service():
    host = REDIS_HOST
    port = "6379"
    db = ""
    password = "lolkek123"

    logging.info(f"Connecting to redis. {host}:{port}")
    service_discovery : sd.ServiceDiscovery = sd.init_and_get_service_discovery(
        host, 
        port, 
        password
    )
    
    service_discovery.register(
        replica_name=REPLICA_NAME, 
        service_host=SERVICE_HOST, 
        service_port=SERVICE_PORT
    )

def unregister_service():
    service_discovery = sd.get_service_discovery()
    logger.debug(f"Ungregister  {REPLICA_NAME}")
    service_discovery.unregister(REPLICA_NAME)

@app.on_event('startup')
def startup_event():
    init_global_variables()
    update_secret_number()
    register_service()


@app.on_event("shutdown")
def shutdown_event():
    unregister_service()


@app.get("/return_secret_number")
def read_item():
    return {
        "secret_number" : storage['secret_number']
    }