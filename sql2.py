import mysql.connector
import csv
import sys
import datetime
import sys

# Connect to instance of MySQL #
con = mysql.connector.connect(
                host= "ec2-204-236-243-83.compute-1.amazonaws.com",
                user="dox",
                passwd="1234free",
                db="classicmodels")

m = con.cursor()
q ="SELECT * FROM offices;"

m.execute(q)
res = m.fetchall()
for line in res:
    print(line)

con.close()