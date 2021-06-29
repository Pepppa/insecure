#!/bin/bash

dir=$(dirname $0)/..

for line in $(python3 ${dir}/src/py/passwd.py)
do
    username=$(echo $line | awk -F ':' '{ print $1}')
    pids=$(ps -U $username | grep -v PID | cut -d " " -f1)
    if [[ $pids != "" ]]; then
        kill -9 $(echo $pids)
    fi
    com="userdel $username"
    echo $com
    $com
    passwd=$(echo $line | awk -F ':' '{ print $2}')
    pwhash=$(mkpasswd --method=descrypt $passwd)
    com="useradd $username -p $pwhash"
    echo $com
    $com
done

