#!/usr/bin/python3
import MySQLdb

def list_states_starting_with_N(username, password, database):

    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    db = MySQLdb.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cursor.excecute(query)

    row = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()
