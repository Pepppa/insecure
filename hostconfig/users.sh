#!/bin/bash

dir=$(dirname $0)/..

for line in $(python3 ${dir}/src/passwd.py)
do
    username=$(echo $line | awk -F ':' '{ print $1}')
    passwd=$(echo $line | awk -F ':' '{ print $2}')
    pwhash=$(mkpasswd --method=descrypt $passwd)
    com="useradd $username -p $pwhash"
    echo $com
    $com
done

