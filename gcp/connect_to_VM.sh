#!/bin/bash

# Include variables and functions defined in 'vars_functions.sh'
source ./vars_functions.sh

# Run script to add SSH key to instance's metadata if it's not present
source ./add_SSH_key.sh

# Get instance's external IP if needed
if [[ -z "$EXTERNAL_IP" ]]; then
    get_External_IP
fi

# Print message before connecting to VM via SSH
echo "Connecting to VM at: $SSH_ADDRESS"

# Connect to VM via SSH
ssh -o StrictHostKeyChecking=no $SSH_ADDRESS
