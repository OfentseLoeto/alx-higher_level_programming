#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connects to a MySQL server and executes a query to retrieve matching states.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=username, 
            passwd=password, database=database_name, port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC""".format(state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
