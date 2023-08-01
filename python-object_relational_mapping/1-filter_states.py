#!/usr/bin/python3
"""List all states with a name starting with an N from hbtn_0e_0_usa"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")

    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'""")
    for row in c.fetchall():
        print(row)

    c.close()
    db.close()
