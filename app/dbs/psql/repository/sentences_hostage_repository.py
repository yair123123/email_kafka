from typing import List

from returns.maybe import Maybe
from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models import SentenceHostage
from app.dbs.psql.database.config import session_factory


def insert_many_sentences_h(sentences: List[SentenceHostage]):
    return all(map(lambda x: isinstance(x, Success), map(lambda x: insert_sentence_hostage(x), sentences)))


def insert_sentence_hostage(sentence: SentenceHostage) -> Result[SentenceHostage, str]:
    with session_factory() as session:
        try:
            session.add(sentence)
            session.commit()
            session.refresh(sentence)
            return Success(sentence)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def get_sentence_hostage_by_id(id: int) -> Maybe[SentenceHostage]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(SentenceHostage, id))
def get_all_sentences_hostage():
    with session_factory() as session:
        return session.query(SentenceHostage).all()