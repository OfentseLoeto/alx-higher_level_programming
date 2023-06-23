#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states(username, password, database):
    """
    Create the database connection
    """
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')
    Base.metadata.bind = engine

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects
    states = session.query(State).order_by(State.id).all()

    # Print the states
    for state in states:
        print(state.id, state.name)

    # Close the session and database connection
    session.close()


if __name__ == '__main__':
    username = 'your_username'
    password = 'your_password'
    database = 'hbtn_0e_6_usa'

    list_states(username, password, database)

