#!/usr/bin/python3
"""List all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities, states WHERE states.name = %s\
AND states.id = cities.state_id ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    print(', '.join(row[0] for row in rows))
    cur.close()
    db.close()
