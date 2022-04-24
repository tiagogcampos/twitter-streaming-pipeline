from tweepy import StreamingClient
from kafka.producer import KafkaProducer


class TwitterStreamingClient(StreamingClient):
    def __init__(self, **kwargs):
        token = kwargs['bearer_token']
        super().__init__(bearer_token=token)
        kafka_brokers = kwargs['kafka_brokers']
        print(f"using kafka brokers {kafka_brokers}")
        self.producer = KafkaProducer(bootstrap_servers=kafka_brokers)
        self.topic: str = kwargs['kafka_topic']

    def on_connect(self):
        print("Connected to twitter api")


    def on_data(self, raw_data):
        print(raw_data.decode('utf-8'))
        self.producer.send(self.topic, raw_data)

    def on_disconnect(self):
        print("Disconnecting")
        return self.disconnect()