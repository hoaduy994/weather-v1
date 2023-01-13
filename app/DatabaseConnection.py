from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_USER = "root"
DB_HOST = "db"
DATABASE = "the_weather"
DBPORT = "3306"

sql_database_url='mysql+pymysql://{}@{}/{}?charset=utf8'.format(DB_USER, DB_HOST, DATABASE)

engine=create_engine(sql_database_url)

sessionLocal=sessionmaker(autocommit=False,bind=engine)

base=declarative_base()