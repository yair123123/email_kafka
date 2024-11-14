from typing import List

from returns.maybe import Maybe
from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models import SentenceExplos
from app.dbs.psql.database.config import session_factory

def insert_many_sentences_e(sentences: List[SentenceExplos]):
    return all(map(lambda x: isinstance(x, Success), map(lambda x: insert_sentence_explos(x), sentences)))


def insert_sentence_explos(sentence:SentenceExplos) -> Result[SentenceExplos,str]:
    with session_factory() as session:
        try:
            session.add(sentence)
            session.commit()
            session.refresh(sentence)
            return Success(sentence)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_sentence_explos_by_id(id:int) -> Maybe[SentenceExplos]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(SentenceExplos,id))
def get_all_sentences_explos():
    with session_factory() as session:
        return session.query(SentenceExplos).all()