# Twitter Streaming Pipeline

Simple data pipeline using the Twitter Streaming API.

Built with the goal of learning the Spark Structured Streaming API and Kafka.

Using:
- Docker and docker-compose for image creation and containers orchestration.
- Tweepy for connecting, consuming the Twitter API.
- Apache Kafka for event streaming from twitter api to spark streams.
- Apache Spark to read from Kafka Topics.


For now, the TwitterStreamingClient only sends a simple sample data.

## Requirements
1. Docker
2. docker-compose v1.29 (?) - I'm using the version 1.29, so I'm not sure if it
   will work with an older version.

## Run
### 
1. Create a file twitter_api_token.txt with your bearer token and put it in the
   root folder of the project (in the future it should be dynamic).
2. Create all and run all containers
```shell
$: docker-compose up -d
```

3. Check if spark is outputting to the console.
```shell
$: docker-compose logs spark
```

