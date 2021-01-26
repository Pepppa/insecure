#!/bin/bash

ids=$(docker ps | grep insecuredata | awk '{ print $1 }')

for id in $ids
do
    echo "docker kill $id"
    docker kill $id
done

kubectl delete deployment,service insecure

make all
