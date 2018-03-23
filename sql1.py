import mysqlclient

db = MySQLdb.connect(host="34.233.120.240",    # your host, usually localhost
                     user="dox",         # your username
                     passwd="password",  # your password
                     db="classicmodels")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM orders")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[0])

db.close()