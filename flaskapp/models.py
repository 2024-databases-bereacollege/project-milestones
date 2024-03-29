from peewee import *

# Database Configuration
################################
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

# Class Definitions
# https://docs.peewee-orm.com/en/latest/peewee/models.html
# class OtherTable (baseModel):
#     otherid = PrimaryKeyField()
#     data = CharField(null=False)

# class Example (baseModel):
#     username = CharField(32,unique=True)
#     description = CharField(255)
#     other = ForeignKeyField(OtherTable)
#     isInt = BooleanField(default=0)
#     isBool = BooleanField()

class member (baseModel):
    memberId = PrimaryKeyField()
    firstName = CharField(32,unique=True)
    lastName = CharField(32,unique=True)
    phoneNumber = CharField(20,unique=True)
    score = IntegerField()
    NumberOfEventsAttended = IntegerField()

class chapter(baseModel):
    chapterName = PrimaryKeyField()
    numberofMembers = IntegerField()
    chapterLead = CharField(32,unique=True)
    memberId = ForeignKeyField(member)
    chapterEmail = CharField(32,unique=True)

class event:
    eventName = PrimaryKeyField()
    venue = CharField(32,unique=True)
    eventDate = DateTimeField(default=datetime.datetime.utcnow)
    attendance = IntegerField()

class demographics:
    memberId = ForeignKeyField(member),
    race = CharField(32,unique=True)
    age = IntegerField()
    gender = CharField(32,unique=True)

class memberAddress:
    memberId = ForeignKeyField(member),
    street = CharField(32,unique=True)
    city = CharField(32,unique=True)
    state =CharField(32,unique=True) 
    zipcode = IntegerField()

class donation: 
    memberId = ForeignKeyField(member),
    item = CharField(32,unique=True)
    monetaryWorth = IntegerField()



