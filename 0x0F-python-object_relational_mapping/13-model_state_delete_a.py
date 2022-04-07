#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    session = Session(engine)
    session.query(State).filter(State.name.contains('a')
                                ).delete(synchronize_session=False)
    session.commit()
    session.close()
