from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import sys

if "pytest" in sys.modules:
    SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://ourexpenses_user:vkWuQcHiN4mvvKlHw8mVoMIkR6CviQNk@dpg-cs8os7tds78s738j26qg-a.oregon-postgres.render.com/ourexpenses"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()