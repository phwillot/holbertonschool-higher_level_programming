#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from model_city import City
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    for city in session.query(State.name, City.id, City.name).join(City):
        print(f"{city[0]}: ({city[1]}) {city[2]}")
