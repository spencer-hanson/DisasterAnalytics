from cassandra.cluster import Cluster
import json

cluster = Cluster(["54.69.163.35"])
session = cluster.connect("disasteranalytics")
# lat long
data = session.execute("select coordinates from tweets limit 10")
with open("data.txt", "w") as f:
    for row in data:
        coords = json.loads(row.coordinates)
        f.write("{} {}\n".format(coords["longitude"], coords["latitude"]))
