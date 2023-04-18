#!/usr/bin/python3
import MySQLdb
import sys

def main():

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC"

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        if row[1][0] == 'N':
        print(row)

    cuR.close()
    db.close()

    if __name__ == "__main__":
        main()
