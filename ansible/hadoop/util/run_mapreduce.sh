#!/bin/bash

hdfs dfs -rmr /output
python3 /tmp/cass_dump.py
hdfs dfs -copyFromLocal data.txt /data.txt
hadoop jar share/hadoop/tools/lib/hadoop-streaming*.jar -file /tmp/mapper.py -mapper /tmp/mapper.py -file /tmp/reducer.py -reducer /tmp/reducer.py -input /data.txt -output /output
hdfs dfs -copyToLocal /output /tmp/output
