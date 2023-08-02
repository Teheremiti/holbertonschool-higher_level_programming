#!/usr/bin/python3
"""List all cities from gbtn_0e_4_usa"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")

    c = db.cursor()
    c.execute("""
              SELECT cities.id, cities.name, states.name
              FROM cities JOIN states
              ON cities.state_id = states.id
              ORDER BY cities.id
              """)
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
