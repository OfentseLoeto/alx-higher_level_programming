#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":


    hbtn_0e_0_usa = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], state_name=sys.argv[4], charset="utf8")

    cursor = hbtn_0e_0_usa.cursor()

    sql = ("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC".format(state_name))

    cursor.execute(sql)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    hbtn_0e_0_usa.close()

