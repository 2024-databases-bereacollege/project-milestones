from peewee import *
from datetime import datetime

# Database Configuration
################################
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

# Class Definitionsa
# https://docs.peewee-orm.com/en/latest/peewee/models.html
class member(baseModel):
    memberid = PrimaryKeyField(db_column='memberid')
    firstname = CharField(100, db_column='firstname')
    lastname = CharField(100, db_column='lastname')
    phonenumber = CharField(100, db_column='phonenumber')
    score = IntegerField(db_column='score')
    # memberaddress = CharField(255, db_column='memberaddress')  # Use lowercase to match the database
    numberofeventsattended = IntegerField(db_column='numberofeventsattended')
   

class chapter(baseModel):
    chaptername = CharField(db_column='chaptername', primary_key=True)
    numberofmembers = IntegerField(db_column='numberofmembers')
    chapterlead = CharField(db_column='chapterlead')
    chapteremail = CharField(db_column='chapteremail')

class event(baseModel):
    eventname = CharField(db_column='eventname', primary_key=True)  # CamelCase as in your PostgreSQL
    venue = CharField(db_column='venue')  # All lowercase because it wasn't quoted in the CREATE TABLE statement
    theme = CharField(db_column='theme')  # All lowercase because it wasn't quoted in the CREATE TABLE statement
    eventdate = DateField(db_column='eventdate')  # CamelCase as in your PostgreSQL
    # numberofmembersattended = IntegerField(db_column='numberofmemebersattended')  # CamelCase with typo as in your PostgreSQL



class donation(baseModel):
    donationId = AutoField(db_column='donationId')
    donorid = ForeignKeyField(member, backref='donations', db_column='donorId')  # Ensure this matches the column name in your DB
    item = CharField(db_column = 'item')
    monetaryWorth = IntegerField(db_column='monetaryworth')







