#!/usr/bin/pytthon3
"""
Start to link classes to the tablein the database
"""
import sys
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql://username:password@localhost:3306/database')

    Base.metadata.create_all(engine)
