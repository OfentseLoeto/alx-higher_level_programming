#!/usr/bin/python3
from sys import argv
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

    # Connecting to mysql server
    db = MySQLdb.connect(
            user=username,
            passwd=password,
            db=database,
            host='localhost',
            port=3306,
            charset="utf8"
            )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER ORDER BY id ASC")

    row = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

 if __name__ == '__main__':
     if len(argv < 1:
             print("Less arguments"):
             else:
             list_all_states()
