#!/usr/bin/python3
"""Prints the rows which name attribute contains a"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    rows = session.query(State).order_by(
        State.id).filter(State.name.contains('a'))
    for row in rows:
        print(f"{row.id}: {row.name}")
    session.close()
