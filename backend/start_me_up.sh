#!/bin/bash

echo "Starting React app"

pm2 start 0 

echo "starting Docker container"

docker compose up -d
