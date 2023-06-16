#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ = "__main__":

    # Connecting to mysql server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cursor = db.cursor()

    # Excecuting a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
