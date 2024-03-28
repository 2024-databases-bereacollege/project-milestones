# Remove objects from the database
psql -c "DROP table IF EXISTS member;"
psql -c "DROP table IF EXISTS chapter;"
psql -c "DROP table IF EXISTS event;"
psql -c "DROP table IF EXISTS demographics;"
psql -c "DROP table IF EXISTS memberAddress;"
psql -c "DROP table IF EXISTS donation;"

# Create tables
< tables.sql psql

# Load data back into database
< data.sql psql
