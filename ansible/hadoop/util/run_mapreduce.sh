#!/bin/bash

hdfs dfs -rmr /output
hdfs dfs -rmr /data.txt
python3 /tmp/cass_dump.py
hdfs dfs -copyFromLocal data.txt /data.txt
hadoop jar /home/hduser/hadoop/share/hadoop/tools/lib/hadoop-streaming*.jar -file /tmp/mapper.py -mapper /tmp/mapper.py -file /tmp/reducer.py -reducer /tmp/reducer.py -input /data.txt -output /output
hdfs dfs -copyToLocal /output /tmp
scp /tmp/output/part-00000 ubuntu@172.31.8.0:/home/ubuntu/DisasterAnalytics/data.txt
