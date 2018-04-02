from searchtweets import ResultStream, gen_rule_payload, load_credentials
from searchtweets import collect_results

#  Function call to load credentials
enterprise_search_args = load_credentials("credentials.twitter_keys.yaml",
                                          yaml_key="search_tweets_enterprise",
                                          env_overwrite=False)

#  Specify timeperiod  year(yyyy) - month(mm) - day(dd) - time(hhmm)
fromdate = "201207220000"
todate = "201208220000"

rule = gen_rule_payload("Earthquake", from_date=fromdate, to_date=todate, results_per_call=100)
print(rule)

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=enterprise_search_args)  # change this if you need to

[print(tweet.all_text, '\n', "Time: ", tweet.created_at_datetime, '\n', "Source:", tweet.generator.get("name"), '\n')
 for tweet in tweets[0:10]]

