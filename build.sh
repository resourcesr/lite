#!/bin/bash
app="resourcesr_lite"
docker build -t ${app} .
docker run -d -p 56733:80 ${app}:latest
