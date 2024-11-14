from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from app.dbs.psql.database.config import Base


class DeviceInfo(Base):
    __tablename__ = "devices_info"
    device_info_id =  Column(Integer,primary_key=True, autoincrement=True)
    browser  = Column(String,nullable=False)
    os = Column(String,nullable=False)
    device_id = Column(String,nullable=False)

    user = relationship("User",back_populates="device_info")