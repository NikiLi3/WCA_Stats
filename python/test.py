import os
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

server_config = {
    'host': 'db',
    'port': 3306,
    'user': 'root',
    'password': os.environ["MYSQL_ROOT_PASSWORD"],
    'database': os.environ["MYSQL_DATABASE"],
}
connection = mysql.connector.connect(**server_config)
cursor = connection.cursor()

query = 'SELECT CAST(LEFT(id,4) AS UNSIGNED) AS year, COUNT(*) AS count FROM Persons GROUP BY year'

df2 = pd.read_sql(query, connection)

fig, ax = plt.subplots()
fig.dpi = 100

ax.bar(df2["year"],df2["count"])
ax.set_title("New competitors by year")
ax.set_xlabel("Year")
ax.set_ylabel("New competitors")
fig.savefig("bild.png", transparent = True)
print("Saved plot")