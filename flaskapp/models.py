from peewee import *

# Database Configuration
################################
mydb = PostgresqlDatabase("postgres",host="db",user="postgres",password="postgres")

class baseModel(Model):
    class Meta:
        database = mydb

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

class Service_Provider(baseModel):
    OrganizationID = CharField(max_length=255, primary_key=True)
    Organization_Name = CharField(max_length=255)
    ContactPerson = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    DateOfStart = DateField()

class Volunteer(baseModel):
    VolunteerID = IntegerField(primary_key=True)
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    Email = CharField(max_length=255)
    Phone = CharField(max_length=20)
    HasRecordAccess = BooleanField()
    
class Neighbor(baseModel):
    NeighborID = IntegerField(primary_key=True)
    VolunteerID = ForeignKeyField(Volunteer, backref='Neighbor')
    Organization = ForeignKeyField(Service_Provider, backref='Neighbor')
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    DateOfBirth = DateField()
    Phone = CharField(max_length=20)
    Location = TextField()
    Email = CharField(max_length=255)
    HasStateID = BooleanField()
    HasPet = BooleanField()
    
class Visit_Record(baseModel):
    RecordID = IntegerField(primary_key=True)
    ServiceOrder = ForeignKeyField(Visit_Service, backref='visit_record')
    Date = DateField()
    NeighborID = ForeignKeyField(Neighbor, backref='visit_record')
    VolunteerID = ForeignKeyField(Volunteer, backref='visit_record')

class Service(baseModel):
    ServiceID = CharField(max_length=255, primary_key=True)
    ServiceType = CharField(max_length=255)
    Organization = ForeignKeyField(Service_Provider, backref='Service')

class Visit_Service(baseModel):
    ServiceOrder = IntegerField(primary_key=True)
    ServiceID = ForeignKeyField(Service, backref='visit_services')
    Description = TextField()
    RecordID = ForeignKeyField(Visit_Record, backref='visit_service')


class Inventory_Usage(baseModel):
    Order_Number = CharField(max_length=255, primary_key=True)
    NameOfItem = CharField(max_length=255)
    RecordID = ForeignKeyField(Visit_Record, backref='Inventory_Usage')
    Description_of_Item = CharField(max_length=255)
    Number_Of_Item_Used = IntegerField()

class Inventory(baseModel):
    Name_Number = CharField(max_length=255, primary_key=True)
    VolunteerID = ForeignKeyField(Volunteer, backref='Inventory')
    Description_of_Item = CharField(max_length=255)
    ExpirationDate = DateField()
    Number_Of_Item = IntegerField()
    Order_Number = ForeignKeyField(Inventory_Usage, backref='Inventory')





