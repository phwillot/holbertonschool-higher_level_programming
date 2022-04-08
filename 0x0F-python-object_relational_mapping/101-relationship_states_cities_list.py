#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        cities = session.query(City).order_by(
            City.id).filter(state.id == City.state_id).all()
        for city in cities:
            print(f"\t{city.id}: {city.name}")
