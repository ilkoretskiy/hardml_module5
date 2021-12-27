#!/bin/bash

export REDIS_HOST=62.84.127.188
export SERVICE_HOST=62.84.125.150

export SERVICE_PORT_1=12100
docker run --rm -d  -p ${SERVICE_PORT_1}:8000 \
    --env REDIS_HOST=${REDIS_HOST} \
    --env SERVICE_HOST=${SERVICE_HOST} \
    --env SERVICE_PORT=${SERVICE_PORT_1} \
    --name hardml5_lesson2_${SERVICE_PORT_1} \
    hardml5_lesson2 

export SERVICE_PORT_2=12101
docker run --rm -d  -p ${SERVICE_PORT_2}:8000 \
    --env REDIS_HOST=${REDIS_HOST} \
    --env SERVICE_HOST=${SERVICE_HOST} \
    --env SERVICE_PORT=${SERVICE_PORT_2} \
    --name hardml5_lesson2_${SERVICE_PORT_2} \
    hardml5_lesson2 

export SERVICE_PORT_3=12102
docker run --rm -d  -p ${SERVICE_PORT_3}:8000 \
    --env REDIS_HOST=${REDIS_HOST} \
    --env SERVICE_HOST=${SERVICE_HOST} \
    --env SERVICE_PORT=${SERVICE_PORT_3} \
    --name hardml5_lesson2_${SERVICE_PORT_3} \
    hardml5_lesson2 


