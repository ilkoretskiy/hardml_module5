#!/bin/bash

export SERVICE_PORT=12100

docker run --rm -d  -p ${SERVICE_PORT}:8000 \
    --name hardml5_lesson2 \
    hardml5_lesson2 


 