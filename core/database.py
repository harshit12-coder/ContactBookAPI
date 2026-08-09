from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

DB_URL=os.getenv("DB_URL")
engine=create_engine(
DB_URL,
pool_size=10,
pool_pre_ping=True,
max_overflow=5,
echo=True
)

SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()