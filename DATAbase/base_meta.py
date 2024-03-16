from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
engine = create_engine("sqlite:///../DB_2.db", echo=True)
Base = DeclarativeBase()
get_session = sessionmaker(engine, autocommit = False)
