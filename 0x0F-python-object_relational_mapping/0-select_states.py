#!/usr/bin/python3
import MySQLdb

def list_states(username, password, database):

    # Connecting to mysql server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Excecuting a query
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetching all the rows
    rows = cursor.fetchall()

    # Showing the results
    for row in rows:
        print(row)

    # Closing the db
    db.close()
