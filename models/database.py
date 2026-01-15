from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url= "postgresql://postgres:1234@localhost:5432/inventory_db"
engine=create_engine(db_url)
session= sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


