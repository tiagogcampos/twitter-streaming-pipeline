import os

from twitter_producer import TwitterStreamingClient
def main():
    with open("/run/secrets/twitter_api_token", 'rb') as f:
        twitter_token = f.read().decode("utf-8").strip('\n')
    assert twitter_token is not None
    kafka_brokers = os.getenv("KAFKA_BROKERS")
    kafka_topic = os.getenv("KAFKA_TOPIC") or "tweets"
    twitter_streaming_client = TwitterStreamingClient(bearer_token=twitter_token, kafka_brokers=kafka_brokers, kafka_topic=kafka_topic)
    twitter_streaming_client.sample()

if __name__ == '__main__':
    main()