# let's write a code to read and write data to tables
# before that, we need to create a table in the target database
# we execute these sql directly in the mysql workbench
'''
CREATE SCHEMA `mutual_fund_ft` ;

CREATE TABLE customer (
  cust_name char(30),
  age int(3),
  employment varchar(25),
  financial_band int(3) NOT NULL CHECK (financial_band IN (1, 2, 3, 4, 5)),
  dob date
);

financial_bands:
1 poor
2 lower middle class
3 middle class
4 upper middle class
5 rich

date is YYYY-MM-DD format

'''

# let's write entries to the table manually
# but before that, we need to establish a connection
import mysql.connector  # connector module in mysql package has class to establish connection to database
import os
from dotenv import dotenv_values  # dotenv package makes it easier to read .env file during runtime
import pandas as pd  # importing pandas as we are planning to create a dataframe with table data

config = dotenv_values("../.env")  # create a .env file with USER, PASSWORD, HOST and DATABASE values for DB connection
# .env should be created at one level higher than current script
print(config['USER'])  # checking that field value is accessible from .env

#print('USER' in os.environ)
#print("current working directory is:", os.getcwd())

'''
mysql_connection = mysql.connector.connect(user=os.environ.get('USER', "USER_NAME")
                                        , password=os.environ.get('PASSWORD', "PASSWORD")
                                        , host=os.environ.get('HOST', "localhost")
                                        , database=os.environ.get('DATABASE', "mutual_fund_ft"))
'''

mysql_connection = mysql.connector.connect(user=config['USER']
                                        , password=config['PASSWORD']
                                        , host=config['HOST']
                                        , database=config['DATABASE'])

mysql_connection.autocommit = False
conn = mysql_connection

cursor = conn.cursor()
sql_write = """insert into customer ( cust_name, age, employment, financial_band, dob) VALUES """
sql_write += """ ( %s, %s, %s, %s, %s ) """
params = ('venkat', '30', 'sfe', '1', '1989-01-17')
cursor.execute(sql_write, params)

conn.commit()
#conn.close()

# now, let's query the table and load to dataframe
sql_query = """select * from customer """
df = pd.read_sql(sql_query, conn)  # this works but we will get a warning. the right way is to use sqlachemy connection
print(df)
conn.close()

# using sqlalchemy connection
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://'+config['USER']+':'+config['PASSWORD']+'@'+config['HOST']+':'
                       +config['PORT']+'/'+config['DATABASE'], echo=False)

data = pd.read_sql(sql_query, engine)
print(data)
engine.dispose()