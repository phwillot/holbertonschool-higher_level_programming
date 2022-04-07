#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
    session.close()
