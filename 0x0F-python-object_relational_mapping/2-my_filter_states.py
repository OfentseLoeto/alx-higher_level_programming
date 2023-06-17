#!/usr/bin/python

import sys
import MySQLdb

if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    db_name=sys.argv[3]
    state_name=sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
