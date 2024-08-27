from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://user:password@localhost:5432/mydatabase', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
