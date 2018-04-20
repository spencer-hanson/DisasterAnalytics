from cassandra.cluster import Cluster
import uuid
import pendulum
from random_words import RandomWords
import random
import json


def insert(session, idv, time, source, txt, coords):
    query = """INSERT INTO disasteranalytics.tweets (id, time, source, txt, coordinates) VALUES ({}, $${}$$, $${}$$, $${}$$, $${}$$)""".format(
        idv, time, source, txt, coords
    )
    session.execute(query)



def random_coord():
    lat_bounds = [24, 49]
    long_bounds = [-124, -44]
    lat = random.randint(lat_bounds[0], lat_bounds[1]+1)
    long = random.randint(long_bounds[0], long_bounds[1]+1)
    return json.dumps({"longitude": long, "latitude": lat})


if __name__ == "__main__":
    cluster = Cluster(["54.69.163.35"])
    session = cluster.connect("disasteranalytics")
    rw = RandomWords()
    for i in range(0, 10000):
        insert(session,
               uuid.uuid4(),
               pendulum.now().to_iso8601_string(),
               "ThisIsASource",
               " ".join(rw.random_words(count=10))[:280],
               random_coord())
