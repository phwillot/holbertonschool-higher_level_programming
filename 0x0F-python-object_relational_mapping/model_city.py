#!/usr/bin/python3
"""Class definition of a City and an instance"""
from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """This class defines the table cities
    id : Integer primary key
    name: String, NOT NULL
    state_id: Integer, foreign key references states.id NOT NULL
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey('states.id'), nullable=False)
