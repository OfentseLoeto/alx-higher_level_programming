#!/usr/bin/python3
import MySQLdb
from sys import argv

def list_all_states():
    # Connecting to mysql server
    db = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            host='localhost',
            port=3306,
            charset="utf8"
            )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == '__main__':
    list_all_states()
