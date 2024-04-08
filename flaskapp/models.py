from peewee import *
from datetime import datetime

# Database Configuration
################################
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

# Class Definitions
# https://docs.peewee-orm.com/en/latest/peewee/models.html
class member (baseModel):
    memberId = PrimaryKeyField()
    firstName = CharField(100)
    lastName = CharField(100)
    phoneNumber = CharField(100)
    score = IntegerField()
    memberAddress = CharField(25),
    NumberOfEventsAttended = IntegerField()

class chapter(baseModel):
    chapterName = PrimaryKeyField(100)
    numberofMembers = IntegerField()
    chapterLead = CharField(100)
    chapterEmail = CharField(100)

class event:
    eventName = PrimaryKeyField(100)
    venue = CharField(100)
    theme = CharField(100)
    eventDate = DateTimeField(default=datetime.datetime.utcnow)
    attendance = IntegerField()

class donation:
    donationId = PrimaryKeyField(), 
    donationId = ForeignKeyField(member),
    item = CharField(50)
    monetaryWorth = IntegerField()



