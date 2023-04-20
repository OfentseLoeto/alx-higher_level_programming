#!/usr/bin/python3
"""
Start link class to table in database 
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.txt.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class state(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, auto_increment=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql://localhost:3306/<database_name>'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True )
    base.metadata.create_all(engine)
