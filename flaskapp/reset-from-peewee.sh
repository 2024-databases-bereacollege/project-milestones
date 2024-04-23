# Remove objects from the database
psql -c "DROP TABLE IF EXISTS Visit_Record;"
psql -c "DROP TABLE IF EXISTS Visit_Service;"
psql -c "DROP TABLE IF EXISTS Volunteer;"
psql -c "DROP TABLE IF EXISTS Neighbor;"
psql -c "DROP TABLE IF EXISTS Service_Providers;"
psql -c "DROP TABLE IF EXISTS Services;"
psql -c "DROP TABLE IF EXISTS Inventory;"
rm -rf migrations
rm -rf migrations.json

pem init

# Use peewee-migrate to create tables from Peewee models
pem add models.Service_Providers
pem add models.Services
pem add models.Volunteer
pem add models.Neighbor
pem add models.Visit_Record
pem add models.Visit_Service
pem add models.Inventory_Usage
pem add models.Inventory

pem watch
pem migrate

rm -rf migrations
rm -rf migrations.json

# Load data back into database
< data.sql psql
