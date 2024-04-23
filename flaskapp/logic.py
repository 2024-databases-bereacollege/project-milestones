from models import *
#WE ARE NOT USING THIS FILE :)

# First example below- Service providers table 
# Service Providers Table ####################################
def get_all_service_providers():
    return Service_Providers.select()

def add_service_provider(organization, contactPerson, email, phone, dateOfStart):
    Service_Providers.create(Organization=organization, ContactPerson=contactPerson, Email=email, Phone=phone, DateOfStart=dateOfStart)

def get_service_provider(organization):
    return Service_Providers.get(Service_Providers.Organization == organization)
###############################################################
