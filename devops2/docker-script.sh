#!/bin/bash

CHECK_NET=$(docker network ls | grep devops)
CONTAINER_NAME="python-test-v2"

if [ "$CHECK_NET" ]; then
    printf "****Docker network already exists****\n\n"
else
    echo "****Creating docker network****"
    docker network create devops
    echo ""
fi

echo "****Starting up the services****"
./docker_up.sh
echo ""

while :
do
    if [ "$( docker container inspect -f '{{.State.Status}}' $CONTAINER_NAME )" == "exited" ]; then 
        echo "****Python has finished. Removing containers****"
        ./docker_down.sh
        break
    fi
done