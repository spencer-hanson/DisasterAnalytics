from searchtweets import ResultStream, gen_rule_payload, load_credentials
from searchtweets import collect_results
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import uuid

cluster = Cluster()
session = cluster.connect("disasteranalytics")


#  Function call to load credentials
enterprise_search_args = load_credentials("credentials.twitter_keys.yaml",
                                          yaml_key="search_tweets_enterprise",
                                          env_overwrite=False)

search_query = "Superbowl"
num_results = 500

#  Specify time period  year(yyyy) - month(mm) - day(dd) - time(hhmm)
fromdate = "200801010000"
todate = "201710070000"

# initialize temporary data structures to hold information
data_collection = [[num_results - 1], [num_results - 1], [num_results - 1], [num_results - 1]]

rule = gen_rule_payload(search_query, from_date=fromdate, to_date=todate, results_per_call=num_results)
print(rule)

tweets = collect_results(rule, max_results=num_results, result_stream_args=enterprise_search_args)

#  iterate through all collected tweet objects

for tweet in tweets[0:num_results]:
    query = "INSERT INTO disasteranalytics.tweets (id, time, source, txt, coordinates) VALUES ({}, $${}$$, $${}$$, $${}$$, $${}$$)".format(
        uuid.uuid4(),
        str(tweet.created_at_datetime),
        str(tweet.generator.get("name")),
        str(tweet.all_text),
        str(tweet.geo_coordinates)
    )
    session.execute(query)

    print(tweet.all_text, '\n', "Time: ", tweet.created_at_datetime, '\n', "Source:", tweet.generator.get("name"), '\n',
          "geo coordinates: ", tweet.geo_coordinates, '\n')
