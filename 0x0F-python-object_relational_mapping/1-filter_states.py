#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":


    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()

