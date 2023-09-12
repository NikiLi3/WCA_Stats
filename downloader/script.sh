#!/bin/bash

#Get current database export date
export CURRENT_EXPORT_DATE=`jq -r '.export_date' "downloads/metadata.json" | head -c 10`

#Get newest database export date
export NEWEST_METADATA=$(curl -s https://www.worldcubeassociation.org/api/v0/export/public)
export NEWEST_EXPORT_DATE=$(echo $NEWEST_METADATA | jq -r '.export_date' | head -c 10)
export NEWEST_EXPORT_URL=$(echo $NEWEST_METADATA | jq -r '.sql_url')

echo "Current db export date: ${CURRENT_EXPORT_DATE}"
echo "Newest db export date: ${NEWEST_EXPORT_DATE}"

if [ "$CURRENT_EXPORT_DATE" != "$NEWEST_EXPORT_DATE" ]; then
    echo "Newer database export available:"

    echo " -> Deleting old export..."
    rm -rf /database/*
    rm -rf /downloads/*

    echo " - > Downloading newest db export..."
    wget -P /downloads -q $(echo $NEWEST_EXPORT_URL)
    # Unzip into db's init directory
    unzip /downloads/WCA_export.sql.zip -d ./downloads
    # Delete unused zip
    rm /downloads/WCA_export.sql.zip
else
    echo "No new database available."
fi

echo "Starting database service..."