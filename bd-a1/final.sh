#!/bin/bash

# Check if a container name or ID is provided as an argument
CONTAINER_IDENTIFIER=$1

if [ -z "$CONTAINER_IDENTIFIER" ]; then
    echo "Error: Please provide a container name or ID as an argument."
    echo "Usage: ./final.sh <container-name-or-id>"
    exit 1
fi

# Create service-result directory if it doesn't exist
mkdir -p service-result

# Copy output files from Docker container to local machine
echo "Copying files from container to local machine..."

# Get container ID (supports both name and ID)
CONTAINER_ID=$(docker ps -qf "name=$CONTAINER_IDENTIFIER")

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: Container '$CONTAINER_IDENTIFIER' is not running."
    exit 1
fi

# Copy preprocessed data file
docker cp $CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv service-result/
echo "Copied res_dpre.csv"

# Copy EDA insight files
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-1.txt service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-2.txt service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-3.txt service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-4.txt service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-5.txt service-result/
echo "Copied EDA insight files"

# Copy visualization files
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis-1-gender.png service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis-2-survival.png service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis-3-age.png service-result/
echo "Copied visualization files"

# Copy K-means results
docker cp $CONTAINER_ID:/home/doc-bd-a1/k.txt service-result/
echo "Copied k.txt"

# Stop the container
echo "Stopping container..."
docker stop $CONTAINER_ID
echo "Container stopped successfully"

echo "All files have been copied to bd-a1/service-result/ and the container has been stopped."