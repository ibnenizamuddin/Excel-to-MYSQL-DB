import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from os.path import join, dirname, realpath
import os
# Solution:
path = "D:/ecw_install/EXCEL Migration To DB/migration/data/"
listoffile = os.listdir(path)

for file in listoffile:
    print(file)
    filename = path + file
    x = file.split(".")
    tablename = x[0]
    engine = create_engine(
        'mysql+mysqlconnector://username:password@localhost:port/dbname', pool_recycle=3600, pool_size=5, echo=False)
    df = pd.read_excel(filename, dtype=str, keep_default_na=False)
    df.to_sql(tablename, con=engine, if_exists='append',chunksize=100,index=False)
