#!/bin/bash

CONNECTIONS=$1
sed -e "/^MAX_CONNECTIONS/ c MAX_CONNECTIONS=$CONNECTIONS/" server.conf