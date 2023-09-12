# WCA Analysis with Python Jupiter Notebook connected to a mysql docker container

## Description

This project will create visual statistics calculated from the oficial WCA public database export.

It will automatically perform multiple steps:
 - download the newest database export
 - initialise a mysql database with this export
 - start a python script that performs SQL requests to the database and creates visualizations of the returned data using matplotlib
 - upload the created images to a GitHub repository
 - the GitHub repository will trigger a  build process that creates a static website

The resulting website will be available via this link: https://nikili3.github.io/WCA_Stats/

## Prerequisites

Insert your GitHub token

You need a **.env** file in the project root directory to define environment variables:
- MYSQL_DATABASE=wca_db
- MYSQL_ROOT_PASSWORD=mysql
- GITHUB_ACCESS_TOKEN=**_[YOUR_GITHUB_TOKEN]_**



## Start docker container and init db:

To create the images and start the containers open a terminal and move to the project root where compose.yml is and execute:

```
docker compose up --build 
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