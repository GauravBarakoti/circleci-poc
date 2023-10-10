#!/bin/bash

set -xe # -x debug mode and -e exits when error
curl localhost 
curl localhost:8081
curl localhost:8082

python3 tests.py

free -g

nproc