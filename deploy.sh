#!/bin/bash

git reset --hard HEAD
git pull origin main

# This script is used to deploy the application to the k3s cluster.
IMAGE_NAME="flux:latest"

# build the docker image
docker build -t $IMAGE_NAME .

# push the docker image to the local registry
docker tag $IMAGE_NAME localhost:5000/$IMAGE_NAME
docker push localhost:5000/$IMAGE_NAME

