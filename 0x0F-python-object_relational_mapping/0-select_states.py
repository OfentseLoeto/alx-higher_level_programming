#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username=sys.argv[1]
    password=sys.argv[2]
    db_name=sys.argv[3]

    # Connecting to mysql server
    hbtn_0e_0_usa = MySQLdb.connect(host="localhost", port=3306, 
            user=username, 
            passwd=password, 
            db=hbtn_0e_0_usa)

    cur = hbtn_0e_0_usa.cursor()

    # Excecuting a query
    query = "SELECT * FROM states ORDER BY id ASC"
    query = cur.execute(query)

    rows_query = cur.fetchall()
    for row in rows_query:
        print(row)

    cur.close()
    hbtn_0e_0_usa.close()
