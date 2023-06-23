#!/usr/bin/pyhton3
"""
python file that contains the class definition
of a State and an instance Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """
    This class defines the states table
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

def create_states_table():
    """
    This function creates a connection to the database
    """
    engine = create_engine('mysql://username:password@localhost:3306/database')

    # Create the table
    Base.metadata.create_all(engine)
    print("States table is created successfully")

if __name__ == '__main__':
    create_states_table()
