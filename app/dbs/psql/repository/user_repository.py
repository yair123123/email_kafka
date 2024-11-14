from returns.maybe import Maybe
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models.User import User
from app.dbs.psql.database.config import session_factory


def insert_user(user:User) -> Result[User,str]:
    with session_factory() as session:
        try:
            session.add(user)
            session.commit()
            session.refresh(user)
            return Success(user)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_user_by_id(id:int) -> Maybe[User]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(User,id))

def get_user_by_email(email:str) -> Maybe[User]:
    with session_factory() as session:
        return Maybe.from_optional(session
                                   .query(User)
                                   .filter(User.email == email)
                                   .first())
