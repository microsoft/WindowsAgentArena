#!/bin/bash

echo "Initializing Compute VM at startup..."

# Install dos2unix
sudo apt-get install -y dos2unix

# Stop dnsmasq running on port 53
sudo systemctl stop systemd-resolved

# Stop nginx running on port 80
sudo service nginx stop 