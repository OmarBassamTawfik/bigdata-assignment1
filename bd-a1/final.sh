#!/bin/bash
# filepath: /Users/alsammany/Documents/Personal/SPRING 25/Big Data/Assignment 1/bigdata-assignment1/bd-a1/final.sh

# Create service-result directory if it doesn't exist
mkdir -p bd-a1/service-result

# Copy output files from Docker container to local machine
echo "Copying files from container to local machine..."

# Get container ID
CONTAINER_ID=$(docker ps -qf "name=bigdata-container")

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: Container 'bigdata-container' is not running."
    exit 1
fi

# Copy preprocessed data file
docker cp $CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
echo "Copied res_dpre.csv"

# Copy EDA insight files
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
echo "Copied EDA insight files"

# Copy visualization file
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis.png bd-a1/service-result/
echo "Copied vis.png"

# Copy K-means results
docker cp $CONTAINER_ID:/home/doc-bd-a1/k.txt bd-a1/service-result/
echo "Copied k.txt"

# Stop the container
echo "Stopping container..."
docker stop $CONTAINER_ID
echo "Container stopped successfully"

echo "All files have been copied to bd-a1/service-result/ and the container has been stopped."