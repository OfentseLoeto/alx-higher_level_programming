#!/usr/bin/python3

import sys
import MySQLdb

def main():

    conn = MySQLdb.connect(
            host="locahost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cur = conn.cursor()
    search = sys.argv[4]

    cur.execute("""SELECT id,name FROM states WHERE name = %s ORDER BY id ASC""", (search,))

            row = cur.fetchall()

            for row in rows:
            print(row)

            cur.close()
            conn.close()

    if __name__ == '__main__':
    main()
