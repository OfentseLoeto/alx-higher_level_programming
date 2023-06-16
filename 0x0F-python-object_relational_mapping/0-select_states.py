#!/usr/bin/python3
import MySQLdb

    # Connecting to mysql server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Excecuting a query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        for column in rows:
            print "%s," %column
            print "\n"

    db.close()
    cursor.close()
