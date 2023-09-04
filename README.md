# WCA Analysis with Python Jupiter Notebook connected to a mysql docker container

## Create image

```
docker build . --no-cache -t mysql_db
```

Builds an image from a Dockerfile from mysql image which copies two sql files (setup.sql and WCA_export.sql)

## Start container from image and mount to volume which persists db

```
docker run -it --rm --name mysql_wca -e MYSQL_ROOT_PASSWORD=pw -v wca_db:/var/lib/mysql -p 8083:3306 mysql_db
```

## Each time new WCA_export is available

```
docker container exec -it mysql_wca bash
```

```
mysql -u root -ppw < setup.sql
```

```
mysql -u root -ppw -D wca_db < WCA_export.sql
```

### Verify correct initialization

```
mysql -u root -ppw
```

```
show databases;
```

```
show tables;
```

Should display names of 16 tables

## Start Jupiter Notebook

Start Anaconda and launch Jupiter Notebook. Browser should open. Navigate to the directory of your python jupiter notebook file (WCA_Queries.ipynb)




## Alternative way to start docker container and init db:

Move the newly downloaded WCA_export file into db/init directory (name does not matter, just needs to be a .sql file; the setup.sql file is no longer required)

To create the image and start the container open a terminal and move into the directory where compose.yml is and execute:

```
docker-compose up
```

Maybe shut down first:

```
docker-compose down && docker-compose up
```

Note: init script will not run if db volume already existed -> Remove old volume:

### Remove old volume to re-trigger mysql initialization from sql file:


Find volume name and delete it: 

```
docker volume ls
```

```
docker volume rm [volume_name]
```


