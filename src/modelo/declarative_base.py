from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

Base = declarative_base()
session = Session()
