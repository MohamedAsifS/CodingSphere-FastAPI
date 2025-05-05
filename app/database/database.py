from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environs import Env

env=Env()
env.read_env()

#Render database URL
DATABASE_URL=env("DATABASE_URL")

# intial database connection
engine=create_engine(DATABASE_URL)
#creating session ready but not actual session
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
# declaring base class for all models
Base=declarative_base()


def get_db():
    """Dependency to get a database session"""
    session=SessionLocal()
    try:
        yield session
    finally:
        session.close()