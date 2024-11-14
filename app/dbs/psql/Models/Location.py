from sqlalchemy import Integer, Column, String, Float
from sqlalchemy.orm import relationship

from app.dbs.psql.database.config import Base


class Location(Base):
    __tablename__ = "locations"
    location_id =  Column(Integer,primary_key=True, autoincrement=True)
    latitude  = Column(Float,nullable=False)
    longitude = Column(Float,nullable=False)
    city = Column(String(100),nullable=False)
    country = Column(String(100),nullable=False)

    user = relationship("User",back_populates="location")