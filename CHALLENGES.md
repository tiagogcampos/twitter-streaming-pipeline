 # Challenges
1. Parse twitter's streaming api data in Spark.
- Not solvable using from_json function. This method returned bunch of nulls
  when parsing the input. Don't really know why yet. 
- Solved using get_json_object function from spark. So much easier to use.

2. Synchronize containers launch.
- Kafka Producer and Consumer can not be launched before Kafka Brokers.
- This was not solved just by using the depends_on flag on compose.yaml file.
- The solution was to add an HEALTHCHECK to the kafka broker service which
  ran a nc command every 5 seconds and checked if the connection was
successfull. 
