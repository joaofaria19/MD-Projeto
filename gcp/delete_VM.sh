#!/bin/bash

# Include variables and functions defined in 'vars_functions.sh'
source ./vars_functions.sh

# Get instance's external IP
get_External_IP

# Delete the instance
gcloud compute instances delete $INSTANCE_NAME \
    --project $PROJECT_ID \
    --zone $ZONE

# Remove instance's external IP from 'known_hosts' file
remove_IP_from_known_hosts
