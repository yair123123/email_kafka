import json
import os


from kafka import KafkaProducer



def produce_hostages(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_HOSTAGES'],
        value=value,
        key="a".encode('utf-8')
    )

def produce_explosion(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_EXPLOS'],
        value=value,
        key="a".encode('utf-8')
    )

def produce_row_data(value):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send(
        os.environ['TOPIC_ROW_DATA'],
        value=value,
        key=value['email'].encode('utf-8')
    )





