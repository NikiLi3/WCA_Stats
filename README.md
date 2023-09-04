# WCA Analysis with Python Jupiter Notebook connected to a mysql docker container

## Start docker container and init db:

Move the newly downloaded WCA_export file into db/init directory (name does not matter, just needs to be a .sql file; the setup.sql file is no longer required)

To create the image and start the container open a terminal and move into the directory where compose.yml is and execute:

```
docker-compose up --build
```

Maybe shut down first:

```
docker-compose down && docker-compose up --build
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

## Start Jupiter Notebook

Start Anaconda application and launch Jupiter Notebook. Browser should open. Navigate to the directory of your python jupiter notebook file (WCA_Queries.ipynb)