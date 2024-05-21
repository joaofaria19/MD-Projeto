#!/bin/bash

# Variables
PROJECT_ID="md-tp-2324"
ZONE="europe-west2-b"

IMAGE_NAME="md-tp-vm-image"
INSTANCE_NAME="md-tp-vm"

MY_USER="md"
PROJECT_DIR_NAME="MD-Projeto"


# Functions
get_script_dir() {
    SCRIPT_DIR=$(dirname $0)
}

read_SSH_public_key() {
    SSH_KEY=$(cat ~/.ssh/id_rsa.pub)
    USER_KEY_PAIR="$MY_USER:$SSH_KEY"
}

get_External_IP() {
    EXTERNAL_IP=$(gcloud compute instances describe $INSTANCE_NAME \
                      --project $PROJECT_ID \
                      --zone $ZONE \
                      --format="get(networkInterfaces[0].accessConfigs[0].natIP)")
    
    SSH_ADDRESS="$MY_USER@$EXTERNAL_IP"
}

remove_IP_from_known_hosts() {
    ssh-keygen -f ~/.ssh/known_hosts -R $EXTERNAL_IP
}
