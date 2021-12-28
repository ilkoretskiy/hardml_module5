#!/bin/bash

export REDIS_HOST=62.84.127.188
export SERVICE_PORT=12100
export SERVICE_HOST=62.84.125.150

# gunicorn main:app --workers 1 --chdir "./impl" --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --graceful-timeout=15  

docker run --rm \
     -p ${SERVICE_PORT}:8000 \
    --env REDIS_HOST=${REDIS_HOST} \
    --env SERVICE_HOST=${SERVICE_HOST} \
    --env SERVICE_PORT=${SERVICE_PORT} \
    --name web_app_${SERVICE_PORT} \
    hardml5_lesson2 


 
