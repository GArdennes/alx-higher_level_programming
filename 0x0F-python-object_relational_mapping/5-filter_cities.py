#!/usr/bin/python3
"""
python script that lists all cities from a database
"""

import MySQLdb
import sys


def main():
    """
    Function that lists cities in database in order
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
        sql_qy = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name
        LIKE %s
        ORDER BY cities.id ASC
        """
        cursor.execute(sql_qy, (state_n, ))
        results = cursor.fetchall()

        print(", ".join(city[0] for city in results))
        db.close()
    except MySQLdb.Error as e:
        sys.exit(1)


if __name__ == "__main__":
    main()
