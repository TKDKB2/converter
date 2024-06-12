from sqlalchemy import Column, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from database import engine


Base = declarative_base()

"""Rule model"""
class Rule(Base):
    __tablename__ = 'rules'

    id = Column(Integer, primary_key=True)
    input_format = Column(String)
    output_format = Column(String)
    flags = Column(String)

def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


