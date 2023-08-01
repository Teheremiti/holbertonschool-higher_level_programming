#!/usr/bin/python3
"""Display all values in states from hbtn_0e_0_usa where name matches
the argument from the command line"""


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
              SELECT * FROM states
              WHERE name LIKE BINARY '{}'
              ORDER BY states.id
              """.format(argv[4]))
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
