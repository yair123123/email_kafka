from typing import List

from app.services.kafka_directory.publishers.publish import (
    produce_row_data,
    produce_hostages, produce_explosion
)


def contains_keyword(sentences: List[str], keyword: str, startswith: bool = False) -> bool:
    for sentence in sentences:
        if (startswith and any(map(lambda x:x.lower().startswith(keyword),sentence.split(" ")))) or (not startswith and keyword in sentence.lower()):
            return True
    return False


def find_and_publish_danger_sentences(email):
    produce_row_data(email)
    sentences = email['sentences']
    if contains_keyword(sentences, "explos", startswith=True):
        produce_explosion(email)
    elif contains_keyword(sentences, "hostage"):
        produce_hostages(email)
