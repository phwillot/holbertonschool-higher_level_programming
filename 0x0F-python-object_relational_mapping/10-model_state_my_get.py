#!/usr/bin/python3
"""Prints the state object with the name passed as argument"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    row = session.query(State).filter(State.name == sys.argv[4]).one_or_none()
    print(row.id if row else "Not found")
    session.close()
