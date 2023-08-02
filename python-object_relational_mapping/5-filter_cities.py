#!/usr/bin/python3
"""List all cities in the state given by the user"""


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
              SELECT cities.name
              FROM cities JOIN states
              ON cities.state_id = states.id
              WHERE states.name LIKE BINARY %s
              ORDER BY cities.id
              """, (argv[4],))

    sep = ""
    for row in c.fetchall():
        print("{}{}".format(sep, row[0]), end="")
        sep = ", "
    print()

    c.close()
    db.close()
