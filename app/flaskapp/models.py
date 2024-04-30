from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict # Allows us to send data as dictionaries
# Database Configuration
db = PostgresqlDatabase("db",host="localhost",user="postgres",password="postgres") #updated from mydb = PostgresqlDatabase("postgres",host="localhost",user="postgres",password="postgres") 
#Changed back to db
class baseModel(Model):
    def to_dict(self):
        return model_to_dict(self)    
    class Meta:
        database = db

class Service_Providers(baseModel):
    OrganizationID = AutoField() #CharField(max_length=255, primary_key=True)
    Organization_Name = CharField(max_length=255)
    ContactPerson = CharField(max_length=255, null=True, blank=True)
    Email = CharField(max_length=255, null=True, blank=True)
    Phone = CharField(max_length=20, null=True, blank=True)
    DateOfStart = DateField()

class Services(baseModel):
    ServiceID = AutoField() #IntegerField(primary_key=True)
    ServiceType = CharField(max_length=255)
    OrganizationID = ForeignKeyField(Service_Providers, backref='services')  # Adjusted for clarity and consistency

class Volunteer(baseModel):
    VolunteerID = AutoField() #IntegerField(primary_key=True)
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    Password = CharField()
    Email = CharField(max_length=255, null=True, blank=True)
    Phone = CharField(max_length=20, null=True, blank=True)
    HasRecordAccess = BooleanField()
    
class Neighbor(baseModel):
    NeighborID = AutoField()
    VolunteerID = ForeignKeyField(Volunteer, backref='neighbor')  # Ensured consistency in backref
    OrganizationID = ForeignKeyField(Service_Providers, backref='neighbor')  # Adjusted for clarity and consistency
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    DateOfBirth = DateField()
    Phone = CharField(max_length=20, null=True, blank=True)
    Location = TextField(null=True, blank=True)  # Changed from Address to Location
    Email = CharField(max_length=255, null=True, blank=True)
    Created_date = DateTimeField(default=datetime.datetime.now)
    HasStateID = BooleanField()
    HasPet = BooleanField()

class Visit_Service(baseModel):
    RecordID = AutoField() #IntegerField(primary_key=True)
    ServiceID = ForeignKeyField(Services, backref='visit_service')
    Description = TextField()
    Date = DateField()

class Visit_Record(baseModel):
    ServiceOrder = AutoField() #IntegerField(primary_key=True)
    NeighborID = ForeignKeyField(Neighbor, backref='visit_record')  # Ensured consistency in backref
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_record')  # Ensured consistency in backref
    RecordID = ForeignKeyField(Visit_Service, backref='visit_record') # Changed to Visit Service


class Inventory_Usage(baseModel):
    Inventory_UseID = AutoField() #IntegerField(primary_key=True)
    NameOfItem = CharField(max_length=255)
    RecordID = ForeignKeyField(Visit_Record, backref='Inventory_Usage')
    Description_of_Item = CharField(max_length=255, null=True, blank=True)
    Number_Of_Item_Used = IntegerField()


class Inventory(baseModel):
    InventoryID = AutoField() #IntegerField(primary_key=True)
    NameOfItem = CharField(max_length=255)
    VolunteerID = ForeignKeyField(Volunteer, backref='inventory')  # Ensured consistency in backref
    Description_of_Item = CharField(max_length=255, null=True, blank=True)
    ExpirationDate = DateField()
    Number_Of_Item = IntegerField()


