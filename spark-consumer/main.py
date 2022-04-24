import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, get_json_object

def main():
    kafka_brokers = os.getenv("KAFKA_BROKERS")
    kafka_topic = os.getenv("KAFKA_TOPIC") or "tweets"
    print(f"kafka brokers: {kafka_brokers}")
    print(f"kafka topic: {kafka_topic}")
    
    print("Building spark session.")
    spark = SparkSession.builder.appName("kafka-consumer").master("local[*]").getOrCreate()
    
    stream = spark.readStream.format("kafka").option("kafka.bootstrap.servers", kafka_brokers).option("checkpointLocation", "/tmp/checkpoint").option("subscribe", kafka_topic).load()
    stream = stream.withColumn("value", col("value").cast("string"))
    stream = stream.withColumn("id", get_json_object(col("value"), "$.data.id"))
    stream = stream.withColumn("text", get_json_object(col("value"), "$.data.text"))
    stream = stream.select("timestamp", "id", "text")
    
    s = stream.writeStream.format("console").option("truncate", "false").outputMode("update").start()

    s.awaitTermination()


if __name__ == '__main__':
    main()
