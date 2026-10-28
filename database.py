from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "mysql+mysqlconnector://root:Chenna123@localhost:3306/electronic_db"
engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)