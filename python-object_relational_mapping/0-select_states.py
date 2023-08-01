#!/usr/bin/python3
"""Task.0 - Get all states"""


from sys import argv
import MySQLdb


db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2], database=argv[3], 
                     port=3306, charset="utf8")

c = db.cursor()
c.execute("""SELECT * FROM states
          ORDER BY states.id""")
for row in c.fetchall():
    print(row)

c.close()
db.close()
