#!/bin/bash

# Include variables and functions defined in 'vars_functions.sh'
source ./vars_functions.sh

# Read SSH public key
read_SSH_public_key

# Get instance's current SSH keys
CURRENT_KEYS=$(gcloud compute instances describe $INSTANCE_NAME \
                    --project $PROJECT_ID \
                    --zone $ZONE \
                    --format="value(metadata.ssh-keys)")

# Check if the 'user:SSH key' pair has already been added to instance's metadata
if [[ $CURRENT_KEYS != *"$USER_KEY_PAIR"* ]]; then

    # Append the new 'user:SSH key' pair to current SSH keys
    METADATA="ssh-keys=$CURRENT_KEYS"$'\n'"$USER_KEY_PAIR"

    # Add SSH public key(s) to the instance
    gcloud compute instances add-metadata $INSTANCE_NAME \
        --project $PROJECT_ID \
        --zone $ZONE \
        --metadata "$METADATA"

    # Get instance's external IP
    get_External_IP

    # Remove instance's external IP from 'known_hosts' file
    remove_IP_from_known_hosts

fi
