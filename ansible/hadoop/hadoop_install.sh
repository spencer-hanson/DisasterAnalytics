#!/bin/bash
apt-get install -y default-jre default-jdk
addgroup hadoop
adduser --disabled-password --gecos "" --ingroup hadoop hduser
echo "$(cat hadoop_conf)" >> /home/hduser/.bashrc
cd /home/ubuntu

ssh-keygen -f aa -t rsa -N ''
mv /home/ubuntu/aa.pub /home/hduser/.ssh/id_rsa.pub
mv /home/ubuntu/aa /home/hduser/.ssh/id_rsa
cp /home/hduser/.ssh/id_rsa.pub /home/hduser/.ssh/authorized_keys
mv start_hadoop.sh /home/hduser
mv stop_hadoop.sh /home/hduser
chown -R hduser:hadoop /home/hduser
chmod u+x /home/hduser/*.sh
mv *.xml /home/hduser/hadoop/etc/hadoop
mv *.sh /home/hduser/hadoop/etc/hadoop
wget -O hadoop.tar.gz https://archive.apache.org/dist/hadoop/core/hadoop-2.7.3/hadoop-2.7.3.tar.gz
mv hadoop.tar.gz /home/hduser
cd /home/hduser
tar xzf hadoop.tar.gz
export HADOOP_HOME=/home/hduser/hadoop
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$HADOOP_HOME/bin
mv hadoop-2.7.3 hadoop
chown -R hduser:hadoop hadoop
mkdir -p /app/hadoop/tmp
chown hduser:hadoop /app/hadoop/tmp
chmod 750 /app/hadoop/tmp
yes | hdfs namenode -format
