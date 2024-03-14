# Remove objects from the database
psql -c "DROP table IF EXISTS member;"
psql -c "DROP table IF EXISTS chapter;"

# Create tables
< tables.sql psql

# Load data back into database
< data.sql psql
