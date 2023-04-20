#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(f'mysql://{mysql_user}:{mysql_password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print('Nothing')
    else:
        print(f'{state.id}: {state.name}')

    session.close()
    engine.dispose()