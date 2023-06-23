#!/usr/bin/pyhton3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

def create_states_table():
    engine = create_engine('mysql://username:password@localhost:3306/database')

    # Create the table
    Base.metadata.create_all(engine)
