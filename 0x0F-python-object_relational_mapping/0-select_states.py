#!/usr/bin/python3
import MySQLdb

def list_states(username, password, database):

    # Connecting to mysql server
    db = MySQLdb.connect(user=username, passwd=password, db=database, host='localhost', port=3306)
    
    cursor = db.cursor()

    query = "SELECT * FROM states ORDER ORDER BY id ASC"
    cursor.execute(query)

    row = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

 if __name__ : "__main__":
     import sys

     username=sys.argv[1]
     password=sys.argv[2]
     database=sys.argv[3]

     list_states(username, password, database)
