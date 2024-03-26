from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = 'postgresql://fastapi:postgres@localhost/fastapi'

engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sqlalchemy.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.declarative_base()


