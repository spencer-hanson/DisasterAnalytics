from cassandra.cluster import Cluster
import json

cluster = Cluster(["172.31.18.195"])
session = cluster.connect("disasteranalytics")
# lat long
counter = 0
data = session.execute("select coordinates from tweets")
with open("data.txt", "w") as f:
    for row in data:
        if counter % 1000 == 0:
            print(counter)
        counter = counter + 1
        coords = json.loads(row.coordinates)
        f.write("{} {}\n".format(coords["latitude"], coords["longitude"]))
