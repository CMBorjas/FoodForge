from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os

# Get the directory where this file is located
basedir = os.path.abspath(os.path.dirname(__file__))

# Create SQLite database in the project directory
DATABASE_PATH = os.path.join(basedir, 'foodforge.db')
DATABASE_URI = f'sqlite:///{DATABASE_PATH}'

# Create engine
engine = create_engine(
    DATABASE_URI,
    echo=False,  # Set to True for SQL query logging
    connect_args={'check_same_thread': False}  # Needed for SQLite
)

# Create session factory
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

# Base class for models
Base = declarative_base()

def init_db():
    """Initialize the database by creating all tables."""
    import models  # Import models to register them with Base
    Base.metadata.create_all(engine)
    print(f"Database initialized at: {DATABASE_PATH}")

def get_session():
    """Get a database session."""
    return Session()

def close_session():
    """Close the current session."""
    Session.remove()
