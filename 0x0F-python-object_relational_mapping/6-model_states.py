#!/usr/bin/python3
"""
Start link class to table in database 
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


def create_states_table():
    """
    Create a connection to the database
    """
    engine = create_engine('mysql://username:password@localhost:3306/database')

    # Create the tables
    Base.metadata.create_all(engine)
    print("States table created successfully!")


if __name__ == '__main__':
    create_states_table()
