from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MARIADB_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/flights'
engine = create_engine(MARIADB_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
