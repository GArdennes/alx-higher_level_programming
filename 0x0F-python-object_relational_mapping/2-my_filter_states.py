#!/usr/bin/python3
"""
python script that lists all states from a database
"""

import MySQLdb
import sys


def main():
    """
    Function for listing states in ascending order
    """
    if len(sys.argv) != 5:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_n = sys.argv[3]
    state_n = sys.argv[4]

    try:
        db = MySQLdb.connect(
                host="localhost",
                user=mysql_username,
                password=mysql_password,
                database=database_n,
                port=3306
                )
        cursor = db.cursor()
        sql_qy = "SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(state_n)
        cursor.execute(sql_qy)
        results = cursor.fetchall()

        for row in results:
            print(row)
        db.close()
    except MySQLdb.Error as e:
        sys.exit(1)


if __name__ == "__main__":
    main()
