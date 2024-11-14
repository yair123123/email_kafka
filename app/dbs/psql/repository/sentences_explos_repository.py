from returns.maybe import Maybe
from returns.result import Failure, Success, Result
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models import SentenceExplos
from app.dbs.psql.database.config import session_factory


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
