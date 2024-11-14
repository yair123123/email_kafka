from typing import List

from app.services.kafka_directory.publishers.publish import producer



def contains_keyword(sentences: List[str], keyword: str, startswith: bool = False) -> (bool, int):
    for x in range(len(sentences)):
        if (startswith and any(map(lambda x: x.lower().startswith(keyword), sentences[x].split(" ")))) or (
                not startswith and keyword in sentences[x].lower()):
            return True, x
    return False, -1


def find_and_publish_danger_sentences(email):
    producer(email,'TOPIC_ROW_DATA')
    sentences = email['sentences']

    found, index = contains_keyword(sentences, "explos", startswith=True)
    if found:
        sentences.insert(0, sentences.pop(index))
        producer(email,'TOPIC_EXPLOS')

    found, index = contains_keyword(sentences, "hostage")
    if found:
        sentences.insert(0, sentences.pop(index))
        producer(email,'TOPIC_HOSTAGES')
