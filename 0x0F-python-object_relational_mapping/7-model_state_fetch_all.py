#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Check number of arguments
    if len(sys.argv) != 4:
        print('Usage: {} username password database'.format(sys.argv[0]))
        sys.exit(1)

    # Connect to database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects and print results
    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))

    # Close session
    session.close()

