import vertica_python

# file login.ini contains host, username, password, and db name
with open('login.ini', 'r') as f:
	host = f.readline().strip()
	username = f.readline().strip()
	password = f.readline().strip()
	database = f.readline().strip()

conn_info = {'host': host,
			 'port': 5433,
			 'user': username,
			 'password': password,
			 'database': database,
			 'read_timeout': 600,
			 'connection_timeout': 5}

connection = vertica_python.connect(**conn_info)
cur = connection.cursor()

dataset = 'testdts'

stm = 'SELECT * FROM ' + dataset

cur.execute(stm)

for row in cur.iterate():
    print(row)