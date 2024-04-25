from models import *  
myappdb.connect()
myappdb.create_tables([Service_Providers, Services, Volunteer, Neighbor, Visit_Record, Visit_Service, Inventory_Usage, Inventory], safe=True)
