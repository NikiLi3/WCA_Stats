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

count = 1


def savefig(figure):
    global count
    figure.savefig("/tmp/cache/image" + str(count) + ".png", transparent=True)
    count += 1


# New competitors by year
query = 'SELECT CAST(LEFT(id,4) AS UNSIGNED) AS year, COUNT(*) AS count FROM Persons GROUP BY year'

df = pd.read_sql(query, connection)

fig, ax = plt.subplots()
fig.dpi = 150

ax.bar(df["year"], df["count"])
ax.set_xlabel("Year")
ax.set_ylabel("New competitors")
savefig(fig)

# Most common nationalities
query = 'SELECT Countries.name AS country, COUNT(DISTINCT(Persons.id)) AS count FROM Persons INNER JOIN Countries ON ' \
        'Persons.countryId=Countries.id GROUP BY country ORDER BY count DESC LIMIT 30'

df = pd.read_sql(query, connection)

fig, ax = plt.subplots()
fig.dpi = 150

ax.bar(df["country"], df["count"])
ax.set_xlabel("Country")
ax.set_ylabel("Number of people from that country")
plt.xticks(rotation=90, ha="center")
savefig(fig)

# Least common nationalities
query = 'SELECT Countries.name AS country, COUNT(DISTINCT(Persons.id)) AS count FROM Persons INNER JOIN Countries ON ' \
        'Persons.countryId=Countries.id GROUP BY country ORDER BY count ASC LIMIT 30'
df = pd.read_sql(query, connection)

fig, ax = plt.subplots()
fig.dpi = 150

ax.bar(df["country"], df["count"])
ax.set_xlabel("Country")
ax.set_ylabel("Number of people from that country")
plt.xticks(rotation=90, ha="center")
savefig(fig)

# Region of origin distribution among WCA competitors
query = "SELECT con.name, COUNT(DISTINCT(p.id)) AS count FROM Persons AS p INNER JOIN Countries ON " \
        "p.countryId=Countries.id INNER JOIN Continents AS con ON Countries.continentId=con.id GROUP BY con.name " \
        "ORDER BY count DESC"

df = pd.read_sql(query, connection)

fig, ax = plt.subplots()
fig.dpi = 150

ax.pie(df["count"], labels=df["name"], autopct='%1.1f%%', startangle=0,
       explode=[0.02 for _ in range(len(df) - 1)] + [0.3])
savefig(fig)
