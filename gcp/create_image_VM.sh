#!/bin/bash

# Include variables and functions defined in 'vars_functions.sh'
source ./vars_functions.sh

# Create the instance from the existing VM image
gcloud compute instances create $INSTANCE_NAME \
    --project $PROJECT_ID \
    --zone $ZONE \
    --source-machine-image $IMAGE_NAME

# Run script to add SSH key to instance's metadata if it's not present
source ./add_SSH_key.sh
