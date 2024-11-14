from collections import Counter
from operator import attrgetter

from toolz import pipe

from app.dbs.psql.repository.sentences_explos_repository import get_all_sentences_explos
from app.dbs.psql.repository.sentences_hostage_repository import get_all_sentences_hostage


def most_word():
    return pipe(
        list(map(attrgetter('sentence'), get_all_sentences_hostage())) + list(
            map(attrgetter('sentence'), get_all_sentences_explos())),
        lambda x: [word for word in "".join(x).replace(".", " ").split(" ")],
        lambda x: (max(Counter(x).most_common(), key=lambda t: t[1])))
