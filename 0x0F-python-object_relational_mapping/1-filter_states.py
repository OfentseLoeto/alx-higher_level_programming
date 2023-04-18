#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE states.id => '4' ORDER BY id ASC")

    print(cursor.fetchall())

    cursor.close()
    db.close()
