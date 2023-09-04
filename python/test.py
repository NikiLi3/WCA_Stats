import pandas as pd
import mysql.connector

server_config = {
    'host': 'db',
    'port': 3306,
    'user': 'root',
    'password': 'mysql',
    'database': 'wca_db',
}
conn = mysql.connector.connect(**server_config)
cursor = conn.cursor()

query = 'SHOW TABLES'
df = pd.read_sql(query, conn)
print(df)

print('db has been connected')