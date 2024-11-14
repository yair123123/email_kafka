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

    location = relationship("Location",back_populates="user",lazy="joined")
    device_info = relationship("DeviceInfo",back_populates="user",lazy="joined")
    sentences_hostage = relationship("SentenceHostage",back_populates="user",lazy="joined")
    sentences_explos = relationship("SentenceExplos",back_populates="user",lazy="joined")
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "username": self.username,
            "ip_address": self.ip_address,
            "created_at": self.created_at,
            'location': self.location.to_dict(),
            'device_info':self.device_info.to_dict(),
            'sentences_hostage': [sentence.sentenc for sentence in self.sentences_hostage],
            'sentences_explos': [sentence.sentence for sentence in self.sentences_explos]        }