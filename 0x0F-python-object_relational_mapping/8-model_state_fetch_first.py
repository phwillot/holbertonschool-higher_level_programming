#!/usr/bin/python3
"""Prints the first State object from the database"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    firstRow = session.query(State).order_by(State.id).first()
    print(f"{firstRow.id}: {firstRow.name}" if firstRow else "Nothing")
    session.close()
