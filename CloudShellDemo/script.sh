#!/bin/bash
echo "Listing the projects"
gcloud projects list

echo ""
echo ""
echo "Listing the configurations"
gcloud config configurations list

echo ""
echo ""
echo "Creating a config for dev environment"
gcloud config configurations create dev-config
gcloud config set core/account <Enter your GCP Account email address>
gcloud config set core/project <Enter your Project id>
gcloud config set compute/region us-central1
gcloud config set compute/zone us-central1-a

echo ""
echo ""
echo "Listing the configurations"
gcloud config configurations list

echo ""
echo ""
echo "Activating the configurations"
gcloud config configurations activate dev-config

echo ""
echo ""
echo "Enabling the compute engine API"
gcloud services enable compute.googleapis.com

echo ""
echo ""
echo "Create a new VM machine"
gcloud compute instances create edureka-vm1 --zone=us-central1-a  --machine-type=f1-micro --image-project=centos-cloud --image-family=centos-7 --boot-disk-type=pd-standard \
--boot-disk-size=20GB

echo ""
echo "Compute engine created successfully"

echo ""
echo ""
echo "Printing virtual machines in project"
gcloud compute instances list

echo "Exiting.."
exit 0
