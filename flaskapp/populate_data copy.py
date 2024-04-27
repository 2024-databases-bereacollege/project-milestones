import random
from models import Service_Providers, Services, Volunteer, Neighbor, Visit_Record, Visit_Service, Inventory_Usage, Inventory
import datetime

fake = Faker()

def generate_random_date(start_date=datetime.date(1950, 1, 1), end_date=datetime.date.today()):
    return fake.date_between(start_date=start_date, end_date=end_date)

def populate_data():
    # Create service providers
    for _ in range(10):
        provider = Service_Providers.create(
            Organization_Name=fake.company(),
            ContactPerson=fake.name(),
            Email=fake.email(),
            Phone=fake.phone_number(),
            DateOfStart=generate_random_date()
        )

    # Create services
    service_types = ["Cleaning", "Grocery Delivery", "Medical Assistance", "Home Repair", "Companionship"]
    for _ in range(20):
        service = Services.create(
            ServiceType=random.choice(service_types),
            OrganizationID=random.choice(Service_Providers.select())
        )

    # Create volunteers
    for _ in range(30):
        volunteer = Volunteer.create(
            FirstName=fake.first_name(),
            LastName=fake.last_name(),
            Password="password",
            Email=fake.email(),
            Phone=fake.phone_number(),
            HasRecordAccess=random.choice([True, False])
        )

    # Create neighbors
    for _ in range(50):
        neighbor = Neighbor.create(
            VolunteerID=random.choice(Volunteer.select()),
            OrganizationID=random.choice(Service_Providers.select()),
            FirstName=fake.first_name(),
            LastName=fake.last_name(),
            DateOfBirth=generate_random_date(),
            Phone=fake.phone_number(),
            Location=fake.Location(),
            Email=fake.email(),
            Created_date=fake.date_time(),
            HasStateID=random.choice([True, False]),
            HasPet=random.choice([True, False])
        )

    # Create visit records
    for _ in range(100):
        visit = Visit_Record.create(
            NeighborID=random.choice(Neighbor.select()),
            VolunteerID=random.choice(Volunteer.select()),
            Date=generate_random_date()
        )

    # Create visit services
    for _ in range(150):
        Visit_Service.create(
            ServiceID=random.choice(Services.select()),
            Description=fake.sentence(),
            RecordID=random.choice(Visit_Record.select())
        )

    # Create inventory usage
    for _ in range(200):
        Inventory_Usage.create(
            NameOfItem=fake.word(),
            RecordID=random.choice(Visit_Record.select()),
            Description_of_Item=fake.sentence(),
            Number_Of_Item_Used=random.randint(1, 10)
        )

    # Create inventory
    for _ in range(100):
        Inventory.create(
            NameOfItem=fake.word(),
            VolunteerID=random.choice(Volunteer.select()),
            Description_of_Item=fake.sentence(),
            ExpirationDate=generate_random_date(),
            Number_Of_Item=random.randint(1, 100),
            Inventory_UseID=random.choice(Inventory_Usage.select())
        )

if __name__ == "__main__":
    populate_data()
