#!/usr/bin/python3

"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def main():

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")
    
    cursor = conn.cursor()

    query = "SELECT id,name FROM states ORDER BY states.id ASC;"
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)

        if __name__ == "__main__":
            main()
