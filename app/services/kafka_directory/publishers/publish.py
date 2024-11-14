import json
import os


from kafka import KafkaProducer



def producer(value,topic):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ[topic],
        value=value,
        key="a".encode('utf-8')
    )




