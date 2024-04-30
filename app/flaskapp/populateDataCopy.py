```python
import random
from models import Service_Providers, Services, Volunteer, Neighbor, Visit_Record, Visit_Service, Inventory_Usage, Inventory
import datetime

# Utility function to generate random dates
def generate_random_date(start_date=datetime.date(1950, 1, 1), end_date=datetime.date.today()):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def populate_data():
    # Sample data
    company_names = ["Alpha Inc", "Beta LLC", "Gamma Corp"]
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie"]
    last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown"]
    service_types = ["Cleaning", "Grocery Delivery", "Medical Assistance", "Home Repair", "Companionship"]
    item_names = ["Hammer", "Wrench", "Screwdriver", "Tape Measure", "Drill"]

    # Create service providers
    for _ in range(10):
        provider = Service_Providers.create(
            Organization_Name=random.choice(company_names),
            ContactPerson=random.choice(first_names) + " " + random.choice(last_names),
            Email=random.choice(first_names).lower() + random.choice(last_names).lower() + "@example.com",
            Phone='555-' + str(random.randint(1000, 9999)),
            DateOfStart=generate_random_date()
        )

    # Cache service providers, volunteers, and services
    providers = list(Service_Providers.select())
    volunteers = list(Volunteer.select())
    services = list(Services.select())

    # Create services
    for _ in range(20):
        service = Services.create(
            ServiceType=random.choice(service_types),
            OrganizationID=random.choice(providers)
        )

    # Create volunteers
    for _ in range(30):
        volunteer = Volunteer.create(
            FirstName=random.choice(first_names),
            LastName=random.choice(last_names),
            Password="password",
            Email=random.choice(first_names).lower() + random.choice(last_names).lower() + "@example.com",
            Phone='555-' + str(random.randint(1000, 9999)),
            HasRecordAccess=random.choice([True, False])
        )

    # Refresh volunteers list after creation
    volunteers = list(Volunteer.select())

    # Create neighbors
    for _ in range(50):
        neighbor = Neighbor.create(
            VolunteerID=random.choice(volunteers),
            OrganizationID=random.choice(providers),
            FirstName=random.choice(first_names),
            LastName=random.choice(last_names),
            DateOfBirth=generate_random_date(),
            Phone='555-' + str(random.randint(1000, 9999)),
            Location="123 Main St",
            Email=random.choice(first_names).lower() + random.choice(last_names).lower() + "@example.com",
            Created_date=datetime.datetime.now(),
            HasStateID=random.choice([True, False]),
            HasPet=random.choice([True, False])
        )

    # Refresh neighbors list after creation
    neighbors = list(Neighbor.select())

    # Create visit records
    for _ in range(100):
        visit = Visit_Record.create(
            NeighborID=random.choice(neighbors),
            VolunteerID=random.choice(volunteers),
            Date=generate_random_date()
        )

    # Refresh visit records list after creation
    visit_records = list(Visit_Record.select())

    # Create visit services
    for _ in range(150):
        Visit_Service.create(
            ServiceID=random.choice(services),
            Description="Performed " + random.choice(service_types),
            RecordID=random.choice(visit_records)
        )

    # Create inventory usage
    for _ in range(200):
        Inventory_Usage.create(
            NameOfItem=random.choice(item_names),
            RecordID=random.choice(visit_records),
            Description_of_Item="Used for " + random.choice(service_types),
            Number_Of_Item_Used=random.randint(1, 10)
        )

    # Refresh inventory usage list after creation
    inventory_usages = list(Inventory_Usage.select())

    # Create inventory
    for _ in range(100):
        Inventory.create(
            NameOfItem=random.choice(item_names),
            VolunteerID=random.choice(volunteers),
            Description_of_Item="Stock item " + random.choice(item_names),
            ExpirationDate=generate_random_date(),
            Number_Of_Item=random.randint(1, 100),
            Inventory_UseID=random.choice(inventory_usages)
        )

if __name__ == "__main__":
    populate_data()
```

###