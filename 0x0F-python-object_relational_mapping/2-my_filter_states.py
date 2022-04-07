#!/usr/bin/python3
"""Displays all values in the states where name match the argument"""
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
        "SELECT id, name FROM states WHERE name = '{}' ORDER BY id".format(
            sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
