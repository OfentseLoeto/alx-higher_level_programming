#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    dtb = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    
    cursor = dtb.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

        cursor.close()
        dtb.close()
