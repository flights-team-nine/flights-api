#!/bin/bash
docker stop $(docker container ls -aq)
docker rm $(docker container ls -aq)
echo Killed