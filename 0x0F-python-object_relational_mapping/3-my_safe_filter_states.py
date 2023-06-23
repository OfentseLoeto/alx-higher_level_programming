#!/usr/bin/python3
"""
script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument,
the script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

def search_states():
    """
    function performs a search operation
    on the states table in a MySQL database
    """
    db = MySQLdb.connect(
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    host='localhost',
    port=3306,
    charset='utf8'
    )
     # Creating a cursor object

    cursor = db.cursor()
    # Retrieving the state name argument
    states_name=argv[4]

    # Constructing the safe query with placeholders
    query = """SELECT * FROM states WHERE name=%s ORDER BY id ASC"""

    # Executing the query with the state name parameter
    cursor.execute(query, (states_name,))

    # Fetching the results
    rows = cursor.fetchall()

    for row in rows:
        print(row)

        cursor.close()
        db.close()

if __name__ == "__main__":
    search_states()
