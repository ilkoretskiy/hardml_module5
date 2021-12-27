#!/bin/bash

export REDIS_HOST=62.84.127.188
export SERVICE_PORT=12100
export SERVICE_HOST=62.84.125.150

docker run --rm -d  -p ${SERVICE_PORT}:8000 \
    --env REDIS_HOST=${REDIS_HOST} \
    --env SERVICE_HOST=${SERVICE_HOST} \
    --env SERVICE_PORT=${SERVICE_PORT} \
    --name hardml5_lesson2 \
    hardml5_lesson2 


 