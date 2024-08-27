from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://student:student1111@147.45.148.218:5432/default_db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
