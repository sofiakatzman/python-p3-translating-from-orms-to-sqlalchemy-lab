#!/usr/bin/env python3

from sqlalchemy import (create_engine, desc,
    Index, Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    def __repr__(self):
        return f"Dog {self.id}: " \
            + f"{self.name}, " \
            + f"Breed {self.breed}"

