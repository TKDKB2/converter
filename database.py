from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:12345678@localhost:5432/converter_dev_pg')

Session = sessionmaker(bind=engine)
session = Session()
