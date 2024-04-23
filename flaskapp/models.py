from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
# Database Configuration
myappdb = PostgresqlDatabase("myappdb",host="localhost",user="postgres",password="postgres") #updated from mydb = PostgresqlDatabase("postgres",host="localhost",user="postgres",password="postgres") 

class baseModel(Model):
    def to_dict(self):
        return model_to_dict(self)    
    class Meta:
        database = myappdb

# Class Definitions
# https://docs.peewee-orm.com/en/latest/peewee/models.html
#class OtherTable (baseModel):
 #   otherid = PrimaryKeyField()
  #  data = CharField(null=False)

#class Example (baseModel):
#    username = CharField(32,unique=True)
#    description = CharField(255)
#    other = ForeignKeyField(OtherTable)
#    isInt = BooleanField(default=0)
#    isBool = BooleanField()

class Service_Providers(BaseModel):
    OrganizationID = CharField(max_length=255, primary_key=True)
    Organization_Name = CharField(max_length=255)
    ContactPerson = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    DateOfStart = DateField()


class Services(BaseModel):
    ServiceID = IntegerField(primary_key=True)
    ServiceType = CharField(max_length=255)
    Organization =


class Volunteer(baseModel):
    VolunteerID = IntegerField(primary_key=True)
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    Password = CharField()
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    HasRecordAccess = BooleanField()

class Service_Provider(baseModel):  # Renamed to singular
    OrganizationID = CharField(max_length=255, primary_key=True)
    OrganizationName = CharField(max_length=255)  # Corrected field name for clarity
    ContactPerson = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    DateOfStart = DateField()

class Services(baseModel):
    ServiceID = IntegerField(primary_key=True)
    ServiceType = CharField(max_length=255)
    OrganizationID = ForeignKeyField(Service_Provider, backref='services')  # Adjusted for clarity and consistency

class Neighbor(baseModel):
    NeighborID = IntegerField(primary_key=True)
    VolunteerID = ForeignKeyField(Volunteer, backref='neighbors')  # Ensured consistency in backref
    OrganizationID = ForeignKeyField(Service_Provider, backref='neighbors')  # Adjusted for clarity and consistency
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    DateOfBirth = DateField()
    Phone = CharField(max_length=20)
    Location = TextField()  # Changed from Address to Location
    Email = CharField(max_length=255)
    Created_date = DateTimeField(default=datetime.datetime.now)
    HasStateID = BooleanField()
    HasPet = BooleanField()

class Visit_Record(baseModel):
    RecordID = IntegerField(primary_key=True)
    NeighborID = ForeignKeyField(Neighbor, backref='visit_records')  # Ensured consistency in backref
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_records')  # Ensured consistency in backref
    Date = DateField()

    NeighborID = ForeignKeyField(Neighbor, backref='visit_record')
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_record')

class Visit_Service(baseModel):
    ServiceOrder = IntegerField(primary_key=True)
    ServiceID = ForeignKeyField(Service, backref='visit_services')
    Description = TextField()
    RecordID = ForeignKeyField(Visit_Record, backref='visit_service')


class Inventory_Usage(baseModel):
    Inventory_UseID = IntegerField(primary_key=True)
    NameOfItem = CharField(max_length=255)
    RecordID = ForeignKeyField(Visit_Record, backref='Inventory_Usage')
    Description_of_Item = CharField(max_length=255)
    Number_Of_Item_Used = IntegerField()


class Inventory(baseModel):
    InventoryID = IntegerField(primary_key=True)
    NameOfItem = CharField(max_length=255)
    VolunteerID = ForeignKeyField(Volunteer, backref='inventory')  # Ensured consistency in backref
    Description_of_Item = CharField(max_length=255)
    ExpirationDate = DateField()
    Number_Of_Item = IntegerField()
    Order_Number = ForeignKeyField(Inventory_Usage, backref='Inventory')

