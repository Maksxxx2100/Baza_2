from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from Config import DB_HOST, DB_PORT, DB_PASSWORD, DB_USER, DB_NAME

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=False)
Base = declarative_base()
get_session = sessionmaker(engine, autocommit = False)
