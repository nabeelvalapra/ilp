#!/bin/sh
# Call this script with the database name
if [ $# -eq 0 ]; then
    echo "Please supply database name as argument. USAGE: `basename $0` databasename"
    exit 1;
fi
echo "######################"
echo "STARTING SCRIPT - POPULATE COMMON TABLES"
echo "######################"
dbname="$1";
#First give permissions to all the other scripts to run
chmod 777 *.sh

#Delete all values first
echo "Deleting existing values in tables"
psql -U klp -d $dbname -f sql/deleteFromTables.sql
echo "Done deleting values..Populating tables now..."
sh populateStatusTable.sh $dbname
sh populateAcademicYear.sh $dbname
sh populateLanguages.sh $dbname

echo "######################"
echo "ENDING SCRIPT - POPULATE COMMON TABLES"
echo "######################"