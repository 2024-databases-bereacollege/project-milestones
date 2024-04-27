import datetime
from models import *

db = PostgresqlDatabase("db", host="localhost", user="postgres", password="postgres")



def generate_sample_data():
    volunteers_sample_data = [
        {"FirstName": "John", "LastName": "Doe", "Password": "hashed_password1", "Email": "john.doe@example.com", "Phone": "555-0101", "HasRecordAccess": True},
        {"FirstName": "Jane", "LastName": "Smith", "Password": "hashed_password2", "Email": "jane.smith@example.com", "Phone": "555-0102", "HasRecordAccess": False},
        {"FirstName": "Emily", "LastName": "Jones", "Password": "hashed_password3", "Email": "emily.jones@example.com", "Phone": "555-0103", "HasRecordAccess": True},
        {"FirstName": "Michael", "LastName": "Brown", "Password": "hashed_password4", "Email": "michael.brown@example.com", "Phone": "555-0104", "HasRecordAccess": False},
        {"FirstName": "Jessica", "LastName": "Davis", "Password": "hashed_password5", "Email": "jessica.davis@example.com", "Phone": "555-0105", "HasRecordAccess": True},
        {"FirstName": "Daniel", "LastName": "Miller", "Password": "hashed_password6", "Email": "daniel.miller@example.com", "Phone": "555-0106", "HasRecordAccess": False},
        {"FirstName": "Laura", "LastName": "Wilson", "Password": "hashed_password7", "Email": "laura.wilson@example.com", "Phone": "555-0107", "HasRecordAccess": True},
        {"FirstName": "Robert", "LastName": "Moore", "Password": "hashed_password8", "Email": "robert.moore@example.com", "Phone": "555-0108", "HasRecordAccess": False},
        {"FirstName": "Linda", "LastName": "Taylor", "Password": "hashed_password9", "Email": "linda.taylor@example.com", "Phone": "555-0109", "HasRecordAccess": True},
        {"FirstName": "William", "LastName": "Anderson", "Password": "hashed_password10", "Email": "william.anderson@example.com", "Phone": "555-0110", "HasRecordAccess": False}
    ]

    neighbors_sample_data = [
        {
            "NeighborID": 1,
            "VolunteerID": 1,  
            "OrganizationID": 8,
            "FirstName": "Alice",
            "LastName": "Johnson",
            "DateOfBirth": datetime.date(1980, 5, 15),
            "Phone": "555-0201",
            "Location": "123 Elm Street, Springfield",
            "Email": "alice.j@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": True,
            "HasPet": False
        },
        {
            "NeighborID": 2,
            "VolunteerID": 2,  
            "OrganizationID": 9,
            "FirstName": "Bob",
            "LastName": "Smith",
            "DateOfBirth": datetime.date(1975, 8, 25),
            "Phone": "555-0202",
            "Location": "456 Maple Avenue, Springfield",
            "Email": "bob.s@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": False,
            "HasPet": True
        },
        {
            "NeighborID": 3,
            "VolunteerID": 3,  
            "OrganizationID": 10,
            "FirstName": "Catherine",
            "LastName": "Williams",
            "DateOfBirth": datetime.date(1992, 11, 30),
            "Phone": "555-0203",
            "Location": "789 Pine Road, Springfield",
            "Email": "catherine.w@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": True,
            "HasPet": True
        }
    ]



    services_sample_data = [
        {"ServiceType": "Meal Delivery", "OrganizationID": "SP002"},
        {"ServiceType": "Legal Aid", "OrganizationID": "SP001"},
        {"ServiceType": "Home Repairs", "OrganizationID": "SP003"},
        {"ServiceType": "Medical Checkup", "OrganizationID": "SP004"},
        {"ServiceType": "Youth Mentoring", "OrganizationID": "SP005"}
    ]

    service_providers_sample_data = [
        {"OrganizationID": "SP006", "Organization_Name": "Springfield Shelter", "ContactPerson": "David Green", "Email": "contact@springfieldshelter.org", "Phone": "555-0301", "DateOfStart": datetime.date(2000, 1, 1)},
        {"OrganizationID": "SP007", "Organization_Name": "Food Bank of Springfield", "ContactPerson": "Eva Turner", "Email": "info@foodbankspringfield.org", "Phone": "555-0302", "DateOfStart": datetime.date(2005, 6, 15)},
        {"OrganizationID": "SP008", "Organization_Name": "Springfield Elderly Care", "ContactPerson": "Franklin Moore", "Email": "care@springfieldelderly.org", "Phone": "555-0303", "DateOfStart": datetime.date(2010, 9, 20)},
        {"OrganizationID": "SP009", "Organization_Name": "Health Clinic", "ContactPerson": "Sara Miles", "Email": "contact@healthclinic.org", "Phone": "555-0304", "DateOfStart": datetime.date(2012, 3, 17)},
        {"OrganizationID": "SP010", "Organization_Name": "Youth Center", "ContactPerson": "Brian Clark", "Email": "info@youthcenter.org", "Phone": "555-0305", "DateOfStart": datetime.date(2015, 7, 10)}
    ]

    visit_services_sample_data = [
        {
            "ServiceOrder": 1,
            "Organization": "Food Bank of Springfield", 
            "NeighborID": 1,  
            "ServiceType": "Meal Delivery",  
            "Description": "Delivered weekly meals to the individual.",
            "VolunteerID": 1, 
        },
        {
            "ServiceOrder": 2,
            "Organization": "Springfield Shelter", 
            "NeighborID": 2,  
            "ServiceType": "Legal Aid", 
            "Description": "Provided legal consultation for housing rights.",
            "VolunteerID": 2,  
        },
        {
            "ServiceOrder": 3,
            "Organization": "Springfield Elderly Care",  
            "NeighborID": 3,  
            "ServiceType": "Home Repairs",  
            "Description": "Assisted in minor home repairs to improve safety.",
            "VolunteerID": 3,  
        }
    ]


    visit_records_sample_data = [
        {"RecordID": 4, "NeighborID": 1, "VolunteerID": 1, "Date": datetime.date(2023, 10, 1)},
        {"RecordID": 5, "NeighborID": 2, "VolunteerID": 2, "Date": datetime.date(2023, 10, 3)},
        {"RecordID": 6, "NeighborID": 3, "VolunteerID": 3, "Date": datetime.date(2023, 10, 5)}
    ]

    inventory_sample_data = [
    {"InventoryID": 1, "NameOfItem": "Canned Beans", "VolunteerID": 1, "Description_of_Item": "Food item", "ExpirationDate": datetime.date(2025, 12, 31), "Number_Of_Item": 100, "Inventory_UseID": 1},
    {"InventoryID": 2, "NameOfItem": "Winter Coats", "VolunteerID": 2, "Description_of_Item": "Clothing item", "ExpirationDate": datetime.date(2024, 11, 30), "Number_Of_Item": 40, "Inventory_UseID": 2},
    {"InventoryID": 3, "NameOfItem": "School Supplies", "VolunteerID": 3, "Description_of_Item": "Educational item", "ExpirationDate": datetime.date(2023, 8, 31), "Number_Of_Item": 200, "Inventory_UseID": 3},
    {"InventoryID": 4, "NameOfItem": "First Aid Kits", "VolunteerID": 4, "Description_of_Item": "Medical item", "ExpirationDate": datetime.date(2025, 1, 15), "Number_Of_Item": 50, "Inventory_UseID": 4},
    {"InventoryID": 5, "NameOfItem": "Flashlights", "VolunteerID": 5, "Description_of_Item": "Utility item", "ExpirationDate": datetime.date(2026, 7, 20), "Number_Of_Item": 75, "Inventory_UseID": 5}
    ]

    inventory_usage_sample_data = [
        {"Inventory_UseID": 1, "NameOfItem": "Canned Beans", "RecordID": 1, "Description_of_Item": "Used for meal preparation", "Number_Of_Item_Used": 10},
        {"Inventory_UseID": 2, "NameOfItem": "Winter Coats", "RecordID": 2, "Description_of_Item": "Distributed to individuals in need", "Number_Of_Item_Used": 5},
        {"Inventory_UseID": 3, "NameOfItem": "School Supplies", "RecordID": 3, "Description_of_Item": "Provided to families for educational support", "Number_Of_Item_Used": 25},
        {"Inventory_UseID": 4, "NameOfItem": "First Aid Kits", "RecordID": 4, "Description_of_Item": "Used in health and safety training sessions", "Number_Of_Item_Used": 3},
        {"Inventory_UseID": 5, "NameOfItem": "Flashlights", "RecordID": 5, "Description_of_Item": "Given for emergency preparedness", "Number_Of_Item_Used": 7}
    ]
    db = PostgresqlDatabase("db", host="localhost", user="postgres", password="postgres")
    
    # Insert the sample data into the database

    with db.atomic():
    #    Volunteer.insert_many(volunteers_sample_data).execute()
    #    Service_Providers.insert_many(service_providers_sample_data).execute()
    #    Services.insert_many(services_sample_data).execute()
    #    Neighbor.insert_many(neighbors_sample_data).execute()
    #    Visit_Record.insert_many(visit_records_sample_data).execute()
    #    Inventory_Usage.insert_many(inventory_usage_sample_data).execute()       
    #    Inventory.insert_many(inventory_sample_data).execute()
    #    Visit_Service.insert_many(visit_services_sample_data).execute()


if __name__ == '__main__':

   
    # Connect to the PostgreSQL database
    db.connect()

    # Generate and insert the sample data
    generate_sample_data()

    # Close the database connection
    db.close()


