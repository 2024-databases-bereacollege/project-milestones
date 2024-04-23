# Remove objects from the database
psql -c "DROP TABLE IF EXISTS Inventory_Usage CASCADE;"
psql -c "DROP TABLE IF EXISTS Inventory CASCADE;"
psql -c "DROP TABLE IF EXISTS Visit_Record CASCADE;"
psql -c "DROP TABLE IF EXISTS Neighbor CASCADE;"
psql -c "DROP TABLE IF EXISTS Services CASCADE;"
psql -c "DROP TABLE IF EXISTS Service_Providers CASCADE;"  
psql -c "DROP TABLE IF EXISTS Volunteer CASCADE;"

# Assuming migrations and migrations.json are related to peewee-migrate
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
pem add models.Inventory_Usage

# Apply migrations to create tables based on models
pem migrate

# Cleaning up migration files after application - optional, consider whether you want to keep these for version control
# rm -rf migrations
# rm -f migrations.json

# Load data back into the database
psql < data.sql





# # Remove objects from the database
# psql -c "DROP TABLE IF EXISTS Visit_Record;"
# psql -c "DROP TABLE IF EXISTS Visit_Service;"
# psql -c "DROP TABLE IF EXISTS Volunteer;"
# psql -c "DROP TABLE IF EXISTS Neighbor;"
# psql -c "DROP TABLE IF EXISTS Service_Providers;"
# psql -c "DROP TABLE IF EXISTS Services;"
# psql -c "DROP TABLE IF EXISTS Inventory;"
# rm -rf migrations
# rm -rf migrations.json

# pem init

# # Use peewee-migrate to create tables from Peewee models
# pem add models.Visit_Record
# pem add models.VisitService
# pem add models.Volunteer
# pem add models.Neighbor
# pem add models.ServiceProviders
# pem add models.Services
# pem add models.Inventory

# pem watch
# pem migrate

# rm -rf migrations
# rm -rf migrations.json

# # Load data back into database
# < data.sql psql
