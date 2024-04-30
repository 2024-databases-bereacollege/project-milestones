# # Remove objects from the database
# psql -c "DROP table IF EXISTS member;"
# psql -c "DROP table IF EXISTS chapter;"
# psql -c "DROP table IF EXISTS event;"
# psql -c "DROP table IF EXISTS donation;"
# #psql -c "DROP table IF EXISTS event_attendance;"

# psql -c "DELETE FROM migratehistory;"
# rm -rf migrations
# rm -rf migrations.json


# ### Added code starts ####################

# Remove objects from the database
psql -c "DROP TABLE IF EXISTS member CASCADE;"
psql -c "DROP TABLE IF EXISTS chapter CASCADE;"
psql -c "DROP TABLE IF EXISTS event CASCADE;"
psql -c "DROP TABLE IF EXISTS donation CASCADE;"
psql -c "DROP TABLE IF EXISTS event_attendance CASCADE;"

psql -c "DELETE FROM migratehistory;"
rm -rf migrations
rm -rf migrations.json

# ### Added code ends ####################

pem init

# Use peewee-migrate to create tables from Peewee models
pem add models.donation
pem add models.member
pem add models.chapter
pem add models.event
pem add models.event_attendance


pem watch
pem migrate

rm -rf migrations
rm -rf migrations.json

# Load data back into database
< data.sql psql
