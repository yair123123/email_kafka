from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.dbs.psql.database.config import Base


class SentenceExplos(Base):
    __tablename__ = "sentences_explos"
    sentence_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    sentence = Column(String(100), nullable=False)

    user = relationship("User", back_populates="sentences_explos")
