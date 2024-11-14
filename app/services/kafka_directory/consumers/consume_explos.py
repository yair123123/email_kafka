import json
import os
from typing import List

from dotenv import load_dotenv
from flask import Flask
from kafka import KafkaConsumer

from app.dbs.psql.Models.SentenceExplos import SentenceExplos
from app.dbs.psql.Models.User import User
from app.dbs.psql.repository.device_info_repository import insert_device_info
from app.dbs.psql.repository.location_repository import insert_location
from app.dbs.psql.repository.sentences_explos_repository import insert_sentence_explos
from app.dbs.psql.repository.user_repository import insert_user
from app.services.save_to_db import save_to_db

load_dotenv(verbose=True)


def consume_sentence_explos():
    consumer = KafkaConsumer(
        os.environ['TOPIC_EXPLOS'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVER'],
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    print('listing...')
    for message in consumer:
        save_to_db(message.value,"E")
        print(f'received: {message.key} : {message.value}')


app = Flask(__name__)
if __name__ == '__main__':
    consume_sentence_explos()
