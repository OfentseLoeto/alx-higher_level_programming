#!/usr/bin/python3
import MySQLdb

def list_states_starting_with_N(username, password, database):

    # Connecting to mysql server
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()

    # Excecuting a query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()
