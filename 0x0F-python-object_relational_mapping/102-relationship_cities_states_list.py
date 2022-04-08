#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)

    states = session.query(State).all()

    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
