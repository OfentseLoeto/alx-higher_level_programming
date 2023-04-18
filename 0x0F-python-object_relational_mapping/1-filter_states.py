#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cu = db.cursor()

    query = ("SELECT * FROM states WHERE name = 'N' ORDER BY id ASC")

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
