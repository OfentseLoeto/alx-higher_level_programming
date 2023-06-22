#!/usr/bin/python3
import MySQLdb
import sys

def search_states():
    '''Check if all arguments are provided'''
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username>, <mysql_password>, <database_name>, <states_name>")
        return

        mysql_username=sys.argv[1]
        mysql_password=sys.argv[2]
        database_name=sys.argv[3]
        state_name=sys.argv[4]

        db = None

        try:
            db = MySQLdb.connect(
                    host='localhost', 
                    port=3306,
                    user='mysql_username',
                    passwd='mysql_password',
                    db='database_name',
                    states='states_name',
                    charset="utf8"
                    )
            cursor = db.cursor()

            query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
            query.execute(query, (states_name,))

            rows = cursor.fetchall()

            if len(rows) > 0:
                for row in rows:
                    print(row)

                else:
                    print("No states found with the provided name")

        except MySQLdb.Error as e:
            print("MySQL Error:", e)

        finally:
            if db:
                cursor.close()
                db.close()

if __name__ == '__main__':
    search_states()

