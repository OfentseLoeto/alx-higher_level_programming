#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":

    if len (sys.argv) != 5:
        print("Usage: {} username password database_name states_name".format(sys.argv[0]))
        exit(1)
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        states_name = sys.argv[4]

        conn = MySQLdb.connect(
                host="hostname",
                port=3306,
                user=user_name,
                passwd=password,
                db=database_name)

        cur = conn.cursor()
        cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC", (states_name))

        row = cur.fetchall()
        for row in rows:
            print(row)

            cur.close()
            conn.close()
