#!/bin/bash
app="resourcesr_lite"
docker build -t ${app} .
docker run --name ${app} -d -p 56733:80 ${app}:latest
