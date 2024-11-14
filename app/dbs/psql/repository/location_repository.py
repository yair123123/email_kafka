from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models.Location import Location
from app.dbs.psql.database.config import session_factory


def insert_location(location:Location) -> Result[Location,str]:
    with session_factory() as session:
        try:
            session.add(location)
            session.commit()
            session.refresh(location)
            return Success(location)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_location_by_id(id:int) -> Maybe[Location]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Location,id))

