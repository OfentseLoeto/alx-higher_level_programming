#!/usr/bin/python3
"""
Script thata list all cities of a given state from
the database hbtn_0e_04_usa
"""

import MySQLdb
from sys import argv

def list_cities_by_state():
    """
    Function that connects to the MySQL server and 
    list all cities of given state
    """
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(argv[0]))
        return

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    try:
        # Connect to the MySQLdb
        db = MySQLdb.connect(host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
        )

        cursor = db.cursor()
        # Construct the query
        query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id ASC"
        cursor.execute(query, (state,))

        rows = cursor.fetchall()
        for row in rows:
            print(rows)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))

    finally:
            if db:
                cursor.close()
                db.close()

if __name__ == "__main__":
    list_cities_by_state()
