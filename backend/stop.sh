#!/bin/bash

echo "stopping React app"

pm2 stop 0

echo "stopping Docker container"

docker compose down

