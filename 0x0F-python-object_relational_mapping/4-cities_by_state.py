#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
 """
import MySQLdb
from sys import argv

def list_cities():
    """
    Function that connects to the MySQL server and lists all cities from the database
    """
    #Create a connection to the database
    db = MySQLdb.connect(host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    #Creating a cursor
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the cities
    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == '__main__':
    list_cities()
