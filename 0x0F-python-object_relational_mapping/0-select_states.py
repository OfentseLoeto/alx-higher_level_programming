#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    db_name=sys.argv[3]

    # Connecting to mysql server
    db = MySQLdb.connect(host="localhost", port=3306, 
            user=username, 
            passwd=password, 
            db=database)

    cur = db.cursor()

    # Excecuting a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        for col in row:
        print("%s," % col
                print "\n"
    cursor.close()
    db.close()
