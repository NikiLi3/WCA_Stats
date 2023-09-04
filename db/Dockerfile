FROM mysql:8.0.34-debian

ADD https://www.worldcubeassociation.org/export/results/WCA_export.sql.zip /docker-entrypoint-initdb.d

RUN apt-get update && apt-get install unzip && unzip /docker-entrypoint-initdb.d/WCA_export.sql.zip -d /docker-entrypoint-initdb.d

