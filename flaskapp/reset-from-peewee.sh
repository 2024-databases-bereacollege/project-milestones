

# Remove objects from the database
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Inventory_Usage CASCADE;"
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Inventory CASCADE;"
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Visit_Record CASCADE;"
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Neighbor CASCADE;"
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Services CASCADE;"
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Service_Providers CASCADE;"  
psql -U postgres -d myappdb -c  "DROP TABLE IF EXISTS Volunteer CASCADE;"

# Cleaning up any existing migration files
rm -rf migrations
rm -f migrations.json

# Initialize peewee-migrate if not already initialized
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

# Apply migrations to create tables based on models
pem migrate

# Cleaning up migration files after application - optional, consider whether you want to keep these for version control
# rm -rf migrations
# rm -f migrations.json

# Load data back into the database
psql < data.sql

