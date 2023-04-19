#!/usr/bin/python3

import sys
import MySQLdb

def main():

    conn = db.MySQLdb.connect(
                           host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database,
                           charset="utf8"
                               )

    cur = conn.cursor()

    query = execute """SELECT cities.name, cities.id states.name
                        FROM cities INNER JOIN states ON cities.state_id=states.id"""
    cur.execute(query)
    row = cur.fetchall()

    for rw in rows:
        print(rw)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
