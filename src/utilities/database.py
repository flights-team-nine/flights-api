from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ

MARIADB_DATABASE_URI = f'mysql+pymysql://{environ.get("DATABASE_USER")}:{environ.get("DATABASE_PASS")}@{environ.get("DATABASE_HOST")}:{environ.get("DATABASE_PORT")}/{environ.get("DATABASE")}'
engine = create_engine(MARIADB_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
