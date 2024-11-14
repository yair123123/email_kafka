import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
load_dotenv(verbose=True)
ENGINE = create_engine(os.environ['ENGINE'])

_session_factory = sessionmaker(bind=ENGINE)
Base = declarative_base()
def session_factory():
    Base.metadata.create_all(ENGINE)
    return _session_factory()