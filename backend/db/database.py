from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

sqlalchemy_database_url = settings.database_url
engine = create_engine(sqlalchemy_database_url)

SesionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()