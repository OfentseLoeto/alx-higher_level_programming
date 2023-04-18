#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1],
    password = sys.argv[2],
    database = sys.srgv[3]


    dtb = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    
    cursor = dtb.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

        cursor.close()
        dtb.close()
