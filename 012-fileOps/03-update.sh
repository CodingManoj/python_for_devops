#!/bin/bash

CONNECTIONS=$1

if [ "$CONNECTIONS" == "" ]; then 
    echo -e "\e[31m Ensure you supply the value of connections in command line \n \t \t \e[0m"
    echo -e "\t Ex: bash update.sh 1245"
    exit 1
fi 

sed -e "/^MAX_CONNECTIONS/ c MAX_CONNECTIONS=$CONNECTIONS" server.conf

