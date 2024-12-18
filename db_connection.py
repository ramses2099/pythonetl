# db_connection.py
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from config import (
    DATABASE_DRIVER,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_USERNAME,
    PORT,
    SERVER,
)


def connect_to_db():
    connect_url= URL.create("mssql+pyodbc",
                            username=DATABASE_USERNAME, 
                            password=DATABASE_PASSWORD,
                            database=DATABASE_NAME,
                            host=SERVER,
                            port=PORT,
                            query={"driver":DATABASE_DRIVER},)
    print(connect_url)
    engine = create_engine(connect_url, echo=False)
    return engine


def test_connect_to_db():
    connect_url = f"mssql+pyodbc://DRIVER={DATABASE_DRIVER};SERVER={SERVER};PORT={PORT};DATABASE={DATABASE_NAME};UID={DATABASE_USERNAME};PWD={DATABASE_PASSWORD};Trusted_Connection=True;"
    engine = create_engine(connect_url, echo=True)
    print(connect_url)
    if engine is not None:
        print("Connected to the database")
#    print(pyodbc.drivers())
