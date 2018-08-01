#!/bin/bash

echo "deb http://www.apache.org/dist/cassandra/debian 36x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -
sudo apt-get -y update
sudo apt-get -y install cassandra

wget -O jre.tar.gz https://www.dropbox.com/s/nr59ymvy8dbcywg/jre-8u152-linux-x64.tar.gz?dl=0
sudo mkdir /opt/jre
sudo tar -zxf jre.tar.gz -C /opt/jre

sudo update-alternatives --install /usr/bin/java java /opt/jre/jre1.8.0_152/bin/java 2000
w