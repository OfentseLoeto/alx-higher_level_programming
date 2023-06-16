#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connecting to mysql server
    db = MySQLdb.connect(host="localhost", port=3306, 
            user=argv[1], 
            password=argv[2], 
            database=argv[3])

    cursor = db.cursor()

    # Excecuting a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        for col in row:
        print("%s," % col
                print "\n"
    cursor.close()
    db.close()
