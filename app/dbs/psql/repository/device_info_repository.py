from returns.maybe import Maybe
from returns.result import Success, Failure, Result
from sqlalchemy.exc import SQLAlchemyError

from app.dbs.psql.Models.DeviceInfo import DeviceInfo
from app.dbs.psql.database.config import session_factory


def insert_device_info(device_info:DeviceInfo) -> Result[DeviceInfo,str]:
    with session_factory() as session:
        try:
            session.add(device_info)
            session.commit()
            session.refresh(device_info)
            return Success(device_info)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_device_info_by_id(id:int) -> Maybe[DeviceInfo]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(DeviceInfo,id))
