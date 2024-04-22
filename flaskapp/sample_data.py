import datetime
from models import *
import psycopg2

myappdb = PostgresqlDatabase("postgres", host="localhost", user="postgres", password="postgres")



def generate_sample_data():
    volunteers_sample_data = [
        {"VolunteerID": 1, "FirstName": "John", "LastName": "Doe", "Password": "hashed_password1", "Email": "john.doe@example.com", "Phone": "555-0101", "HasRecordAccess": True},
        {"VolunteerID": 2, "FirstName": "Jane", "LastName": "Smith", "Password": "hashed_password2", "Email": "jane.smith@example.com", "Phone": "555-0102", "HasRecordAccess": False},
        {"VolunteerID": 3, "FirstName": "Emily", "LastName": "Jones", "Password": "hashed_password3", "Email": "emily.jones@example.com", "Phone": "555-0103", "HasRecordAccess": True},
        {"VolunteerID": 4, "FirstName": "Michael", "LastName": "Brown", "Password": "hashed_password4", "Email": "michael.brown@example.com", "Phone": "555-0104", "HasRecordAccess": False},
        {"VolunteerID": 5, "FirstName": "Jessica", "LastName": "Davis", "Password": "hashed_password5", "Email": "jessica.davis@example.com", "Phone": "555-0105", "HasRecordAccess": True},
        {"VolunteerID": 6, "FirstName": "Daniel", "LastName": "Miller", "Password": "hashed_password6", "Email": "daniel.miller@example.com", "Phone": "555-0106", "HasRecordAccess": False},
        {"VolunteerID": 7, "FirstName": "Laura", "LastName": "Wilson", "Password": "hashed_password7", "Email": "laura.wilson@example.com", "Phone": "555-0107", "HasRecordAccess": True},
        {"VolunteerID": 8, "FirstName": "Robert", "LastName": "Moore", "Password": "hashed_password8", "Email": "robert.moore@example.com", "Phone": "555-0108", "HasRecordAccess": False},
        {"VolunteerID": 9, "FirstName": "Linda", "LastName": "Taylor", "Password": "hashed_password9", "Email": "linda.taylor@example.com", "Phone": "555-0109", "HasRecordAccess": True},
        {"VolunteerID": 10, "FirstName": "William", "LastName": "Anderson", "Password": "hashed_password10", "Email": "william.anderson@example.com", "Phone": "555-0110", "HasRecordAccess": False}
    ]

    neighbors_sample_data = [
        {
            "NeighborID": 1,
            "VolunteerID": 1,  # Assuming a Volunteer with this ID exists
            "Organization": "Helping Hands",
            "FirstName": "Alice",
            "LastName": "Johnson",
            "DateOfBirth": datetime.date(1980, 5, 15),
            "Phone": "555-0201",
            "Address": "123 Elm Street, Springfield",
            "Email": "alice.j@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": True,
            "HasPet": False
        },
        {
            "NeighborID": 2,
            "VolunteerID": 2,  # Adjust based on your data
            "Organization": "Community Support",
            "FirstName": "Bob",
            "LastName": "Smith",
            "DateOfBirth": datetime.date(1975, 8, 25),
            "Phone": "555-0202",
            "Address": "456 Maple Avenue, Springfield",
            "Email": "bob.s@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": False,
            "HasPet": True
        },
        {
            "NeighborID": 3,
            "VolunteerID": 3,  # Adjust based on your data
            "Organization": "Local Aid",
            "FirstName": "Catherine",
            "LastName": "Williams",
            "DateOfBirth": datetime.date(1992, 11, 30),
            "Phone": "555-0203",
            "Address": "789 Pine Road, Springfield",
            "Email": "catherine.w@example.com",
            "Created_date": datetime.datetime.now(),
            "HasStateID": True,
            "HasPet": True
        }
    ]
    services_sample_data = [
        {
            "ServiceType": "Meal Delivery",
            "Organization": "Food Bank of Springfield",  # Adjust based on your data
        },
        {
            "ServiceType": "Legal Aid",
            "Organization": "Springfield Shelter",  # Adjust based on your data
        },
        {
            "ServiceType": "Home Repairs",
            "Organization": "Springfield Elderly Care",  # Adjust based on your data
        }
    ]

    service_providers_sample_data = [
        {
            "Organization": "Springfield Shelter",
            "ContactPerson": "David Green",
            "Email": "contact@springfieldshelter.org",
            "Phone": "555-0301",
            "DateOfStart": datetime.date(2000, 1, 1)
        },
        {
            "Organization": "Food Bank of Springfield",
            "ContactPerson": "Eva Turner",
            "Email": "info@foodbankspringfield.org",
            "Phone": "555-0302",
            "DateOfStart": datetime.date(2005, 6, 15)
        },
        {
            "Organization": "Springfield Elderly Care",
            "ContactPerson": "Franklin Moore",
            "Email": "care@springfieldelderly.org",
            "Phone": "555-0303",
            "DateOfStart": datetime.date(2010, 9, 20)
        }
    ]

    inventory_sample_data = [
        {
            "NameOfItem": "Canned Beans",
            "VolunteerID": 1,  # Assuming a Volunteer with this ID exists
            "ExpirationDate": datetime.date(2025, 12, 31),
            "NumberOfItem": 100,
        },
        {
            "NameOfItem": "Winter Coats",
            "VolunteerID": 2,  # Adjust based on your data
            "ExpirationDate": datetime.date(2024, 11, 30),
            "NumberOfItem": 40,
        },
        {
            "NameOfItem": "School Supplies",
            "VolunteerID": 3,  # Adjust based on your data
            "ExpirationDate": datetime.date(2023, 8, 31),
            "NumberOfItem": 200,
        }
    ]

    visit_services_sample_data = [
        {
            "ServiceOrder": 1,
            "Organization": "Food Bank of Springfield",  # Adjust based on your data
            "NeighborID": 1,  # Adjust based on your data
            "ServiceType": "Meal Delivery",  # Adjust based on your data
            "Description": "Delivered weekly meals to the individual.",
            "VolunteerID": 1,  # Adjust based on your data
        },
        {
            "ServiceOrder": 2,
            "Organization": "Springfield Shelter",  # Adjust based on your data
            "NeighborID": 2,  # Adjust based on your data
            "ServiceType": "Legal Aid",  # Adjust based on your data
            "Description": "Provided legal consultation for housing rights.",
            "VolunteerID": 2,  # Adjust based on your data
        },
        {
            "ServiceOrder": 3,
            "Organization": "Springfield Elderly Care",  # Adjust based on your data
            "NeighborID": 3,  # Adjust based on your data
            "ServiceType": "Home Repairs",  # Adjust based on your data
            "Description": "Assisted in minor home repairs to improve safety.",
            "VolunteerID": 3,  # Adjust based on your data
        }
    ]

    visit_records_sample_data = [
        {
            "RecordID": 1,
            "ServiceOrder": 1,  # Adjust based on your data
            "Date": datetime.date(2023, 10, 1),
            "Time": datetime.datetime.strptime("14:00", "%H:%M").time(),
            "Notes": "Client was very appreciative of the meals.",
        },
        {
            "RecordID": 2,
            "ServiceOrder": 2,  # Adjust based on your data
            "Date": datetime.date(2023, 10, 3),
            "Time": datetime.datetime.strptime("10:30", "%H:%M").time(),
            "Notes": "Follow-up needed to check on legal paperwork.",
        },
        {
            "RecordID": 3,
            "ServiceOrder": 3,  # Adjust based on your data
            "Date": datetime.date(2023, 10, 5),
            "Time": datetime.datetime.strptime("09:00", "%H:%M").time(),
            "Notes": "Repairs completed successfully. Consider safety audit.",
        }
    ]

    # Insert the sample data into the database
    with myappdb.atomic():
        Volunteer.insert_many(volunteers_sample_data).execute()



# for volunteer_data in volunteers_sample_data:
#     Volunteer.create(**volunteer_data)

# for service_data in services_sample_data:
#     Services.create(**service_data)

# for inventory_data in inventory_sample_data:
#     Inventory.create(**inventory_data)

# for neighbor_data in neighbors_sample_data:
#     Neighbor.create(**neighbor_data)

# for provider_data in service_providers_sample_data:
#     Service_Providers.create(**provider_data)

# for visit_service_data in visit_services_sample_data:
#     Visit_Service.create(**visit_service_data)

# for visit_record_data in visit_records_sample_data:
#     Visit_Record.create(**visit_record_data)
