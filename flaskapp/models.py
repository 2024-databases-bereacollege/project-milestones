from peewee import *
import datetime

# Database Configuration
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb
        
class Volunteer(baseModel):
    VolunteerID = IntegerField(primary_key=True)
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    Password = CharField()
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    HasRecordAccess = BooleanField()
    
class Neighbor(baseModel):
    NeighborID = IntegerField(primary_key=True)
    VolunteerID = ForeignKeyField(Volunteer, backref='neighbors')
    Organization = CharField(max_length=255)
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    DateOfBirth = DateField()
    Phone = CharField(max_length=20)
    Address = TextField()
    Email = CharField(max_length=255)
    Created_date = DateTimeField(default=datetime.datetime.now)
    HasStateID = BooleanField()
    HasPet = BooleanField()

class Service_Providers(baseModel):
    Organization = CharField(max_length=255, primary_key=True)
    ContactPerson = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    DateOfStart = DateField()

class Services(baseModel):
    ServiceType = CharField(max_length=255, primary_key=True)
    Organization = ForeignKeyField(Service_Providers, backref='services')

class Inventory(baseModel):
    NameOfItem = CharField(max_length=255, primary_key=True)
    VolunteerID = ForeignKeyField(Volunteer, backref='inventory')
    ExpirationDate = DateField()
    NumberOfItem = IntegerField()

class Visit_Service(baseModel):
    ServiceOrder = IntegerField(primary_key=True)
    Organization = ForeignKeyField(Service_Providers, backref='visit_services')
    NeighborID = ForeignKeyField(Neighbor, backref='visit_services')
    ServiceType = ForeignKeyField(Services, backref='visit_services')
    Description = TextField()
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_services')

class Visit_Record(baseModel):
    RecordID = IntegerField(primary_key=True)
    ServiceOrder = ForeignKeyField(Visit_Service, backref='visit_records')
    Date = DateField()
    Time = DateField()
    Notes = TextField()