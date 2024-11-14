from typing import List

from app.dbs.psql.Models.DeviceInfo import DeviceInfo
from app.dbs.psql.Models.Location import Location
from app.dbs.psql.Models.SentenceExplos import SentenceExplos
from app.dbs.psql.Models.SentenceHostage import SentenceHostage
from app.dbs.psql.Models.User import User
from app.dbs.psql.repository.device_info_repository import insert_device_info
from app.dbs.psql.repository.location_repository import insert_location
from app.dbs.psql.repository.sentences_explos_repository import insert_sentence_explos, insert_many_sentences_e
from app.dbs.psql.repository.sentences_hostage_repository import insert_sentence_hostage, insert_many_sentences_h
from app.dbs.psql.repository.user_repository import insert_user


def save_to_db(message,type_sentence):

    location_id = insert_location(Location(**message['location'])).unwrap().location_id
    device_id = insert_device_info(DeviceInfo(**message['device_info'])).unwrap().device_info_id
    only_user = {k: v for k,v in message.items() if isinstance(v, str)}
    only_user.pop('id')
    only_user['location_id'] = location_id
    only_user['device_id'] = device_id
    user_id = insert_user(User(**only_user)).value_or(0).user_id
    if type_sentence == 'E':
        sentences_explos: List[SentenceExplos] = [SentenceExplos(sentence=sentence,
                                                                 user_id=user_id) for sentence in
                                                  message['sentences']]

        insert_many_sentences_e(sentences_explos)
    if type_sentence == 'H':
        sentences_hostage: List[SentenceHostage] = [SentenceHostage(sentence=sentence,
                                                                 user_id=user_id) for sentence in
                                                  message['sentences']]

        insert_many_sentences_h(sentences_hostage)