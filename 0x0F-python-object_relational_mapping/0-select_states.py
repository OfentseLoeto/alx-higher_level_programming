#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main___":
    
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.arg[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    cursor = cursor.fetchall()
    
    for row in rows:
        print(row)

        cursor.close()
        db.close()
