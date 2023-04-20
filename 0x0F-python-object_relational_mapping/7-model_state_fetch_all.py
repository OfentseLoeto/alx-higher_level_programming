#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # Get command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(f'mysql://{mysql_user}:{mysql_password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects and print them out
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

    # Close session and engine
    session.close()
    engine.dispose()
