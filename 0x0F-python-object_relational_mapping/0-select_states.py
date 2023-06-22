#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":

    # Connecting to mysql server
    conn = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            host='localhost',
            port=3306,
            charset="utf8"
            )
    
    cursor = conn.cursor()

    cursor.execute(""" SELECT * FROM states ORDER BY states.id ASC """)
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
