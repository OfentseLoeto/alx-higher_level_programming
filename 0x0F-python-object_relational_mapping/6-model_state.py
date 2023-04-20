#!/usr/bin/python3
"""
Start link class to table in database 
"""
from sqlalchemy.txt.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine('MySQL://username:password@localhost:3306/mydatabase')
    Base.metadata.create_all(engine)
