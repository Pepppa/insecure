#!/bin/bash

ids=$(docker ps | tail -2 | awk '{ print $1 }')

for id in $ids
do
    echo "docker kill $id"
    docker kill $id
done

make docker-run
