from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file will be created in the same folder as this file
SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# connect_args is needed only for SQLite to allow it to be used
# with multiple threads (FastAPI can use more than one)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is a factory that creates new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that our ORM models will inherit from
Base = declarative_base()
