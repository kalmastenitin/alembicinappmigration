from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app import config


host = config.db_host
username = config.db_username
db_pass = config.db_secret
db_port = config.db_port
db_name = config.db_name


def create_db_url():
    return "mysql+pymysql://{}:{}@{}:{}/{}".format(username, db_pass, host, db_port, db_name)


engine = create_engine(create_db_url(), pool_recycle=300, pool_size=0,
                       max_overflow=-1, pool_use_lifo=True, connect_args={'connect_timeout': 10})
SessionLocal = sessionmaker(
    autoflush=True, expire_on_commit=True, bind=engine)
Base = declarative_base()
