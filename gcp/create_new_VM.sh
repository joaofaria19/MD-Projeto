#!/bin/bash

# Include variables and functions defined in 'vars_functions.sh'
source ./vars_functions.sh

# Instance details
MACHINE_TYPE="n1-highmem-2"                        # N1 series standard machine 1 (1 vCPUs and 3.75 GB RAM)
ACCELERATOR_TYPE="nvidia-tesla-t4"                  # GPU type
ACCELERATOR_COUNT=1                                 # Number of GPUs
IMAGE_FAMILY="common-cu122-ubuntu-2204"             # Deep Learning VM with CUDA 12.2 image
IMAGE_PROJECT="deeplearning-platform-release"       # Deep Learning VM with CUDA 12.2 image project
BOOT_DISK_TYPE="pd-ssd"                             # Persistent SSD boot disk
BOOT_DISK_SIZE="100GB"                              # 100 GB boot disk size
PROVISIONING_MODEL="SPOT"                           # Availability policies

# Read SSH public key
read_SSH_public_key
METADATA="ssh-keys=$USER_KEY_PAIR"

# Create the instance
gcloud compute instances create $INSTANCE_NAME \
    --project $PROJECT_ID \
    --zone $ZONE \
    --accelerator type=$ACCELERATOR_TYPE,count=$ACCELERATOR_COUNT \
    --machine-type $MACHINE_TYPE \
    --image-family $IMAGE_FAMILY \
    --image-project $IMAGE_PROJECT \
    --boot-disk-type $BOOT_DISK_TYPE \
    --boot-disk-size $BOOT_DISK_SIZE \
    --provisioning-model $PROVISIONING_MODEL \
    --metadata "$METADATA"

# Get instance's external IP
get_External_IP

# Remove instance's external IP from 'known_hosts' file
remove_IP_from_known_hosts
