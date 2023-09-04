FROM debian as downloader

ADD https://www.worldcubeassociation.org/export/results/WCA_export.sql.zip ./

RUN apt-get update && apt-get install unzip && unzip WCA_export.sql.zip -d ./

FROM mysql

COPY --from=downloader /WCA_export.sql /docker-entrypoint-initdb.d
