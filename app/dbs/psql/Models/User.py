from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.dbs.psql.database.config import Base


class User(Base):
    __tablename__ = "users"
    user_id =  Column(Integer,primary_key=True, autoincrement=True)
    email  = Column(String(100),nullable=False)
    username = Column(String(100),nullable=False)
    ip_address = Column(String(100),nullable=False)
    created_at = Column(String(100),nullable=False)
    location_id = Column(Integer, ForeignKey("locations.location_id"))
    device_id = Column(Integer, ForeignKey("devices_info.device_info_id"))

    location = relationship("Location",back_populates="user")
    device_info = relationship("DeviceInfo",back_populates="user")
    sentences_hostage = relationship("SentenceHostage",back_populates="user")
    sentences_explos = relationship("SentenceExplos",back_populates="user")