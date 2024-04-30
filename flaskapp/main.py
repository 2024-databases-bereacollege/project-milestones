from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *



app = Flask(__name__)

app.config.from_object(__name__)
CORS(app)

db.connect()
#db.create_tables([Volunteer], safe=True)

# ADD VISIT SECTION ##########################################
def get_neighborsAV():
    neighbors_query = Neighbor.select(
        Neighbor.NeighborID,
        Neighbor.FirstName,
        Neighbor.LastName
    )

    neighbors_list = [
        {
            'NeighborID': neighbor.NeighborID,
            'FullName': f"{neighbor.FirstName} {neighbor.LastName}"
        } for neighbor in neighbors_query
    ]
    return neighbors_list

def get_volunteersAV():
    volunteers_query = Volunteer.select(
        Volunteer.VolunteerID, 
        Volunteer.FirstName, 
        Volunteer.LastName
    )
    return [{
        'VolunteerID': volunteer.VolunteerID,
        'FullName': f"{volunteer.FirstName} {volunteer.LastName}"
    } for volunteer in volunteers_query]


def get_servicesAV():
    services_query = Services.select()
    return [{
        'ServiceID': service.ServiceID,
        'ServiceType': service.ServiceType
    } for service in services_query]

def get_inventoryAV():
    inventory_query = Inventory.select()
    return [{
        'InventoryID': inventory.InventoryID,
        'NameOfItem': inventory.NameOfItem,
        'Number_Of_Item': inventory.Number_Of_Item
    } for inventory in inventory_query]


@app.route('/api/Add_Visit', methods=['GET'])
def get_visit(): 
    data = {
        'neighbors': get_neighborsAV(),
        'volunteers': get_volunteersAV(),
        'services': get_servicesAV(),
        'inventory': get_inventoryAV()
    }
    return jsonify(data)

##############################################################



@app.route('/api/volunteers', methods=['GET']) #GET request to get all volunteers
def get_volunteers():
    # Query all volunteers from the database
    query = Volunteer.select()
    volunteers = [volunteer.to_dict() for volunteer in query]  # Convert models to dictionaries
    
    return jsonify(volunteers)

@app.route('/api/volunteers', methods=['PUT']) #PUT request to update a volunteer
def update_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'error': 'Volunteer not found'}), 404

    data = request.get_json()
    print("Received data for update:", data) 

    for key, value in data.items():
        if hasattr(volunteer, key):  
            setattr(volunteer, key, value)

    db.session.commit()  # TODO adjust from session
    return jsonify(volunteer.to_dict()), 200

################ volunteers below ############################
@app.route('/api/volunteers', methods=['DELETE']) #DELETE request to delete a volunteer
def delete_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'error': 'Volunteer not found'}), 404

    db.session.delete(volunteer)
    db.session.commit()
    return jsonify({'success': 'Volunteer deleted'}), 200

@app.route('/api/volunteers', methods=['POST'])
def add_volunteer():
    try:
        data = request.get_json()
        app.logger.info('Received data: %s', data)

        if not all(key in data for key in ['FirstName', 'LastName', 'Password', 'Email', 'Phone', 'HasRecordAccess']):
            app.logger.error('Missing one or more required fields')
            return jsonify({"error": "Missing data for one or more fields"}), 400

        volunteer = Volunteer.create(
            first_name=data['FirstName'],
            last_name=data['LastName'],
            password=generate_password_hash(data['Password']),
            email=data['Email'],
            phone=data['Phone'],
            has_record_access=data['HasRecordAccess']
        )
        app.logger.info('Volunteer created with ID: %s', volunteer.id)

        return jsonify({
            "id": volunteer.id,
            "first_name": volunteer.first_name,
            "last_name": volunteer.last_name,
            "email": volunteer.email,
            "phone": volunteer.phone,
            "has_record_access": volunteer.has_record_access
        }), 201
    except Exception as e:
        app.logger.error('Error adding volunteer: %s', e, exc_info=True)
        return jsonify({"error": str(e)}), 500

################ volunteers above ############################
    
################ neighbors below ############################    
@app.route('/api/neighbors', methods=['GET'])
def get_neighbors():
    neighbors = [neighbor.to_dict() for neighbor in Neighbor.select()]
    return jsonify(neighbors)


################ neighbors above ############################



@app.route('/api/service_providers', methods=['GET'])
def get_service_providers():
    query = Service_Providers.select()
    service_providers = [provider.to_dict() for provider in query]
    return jsonify(service_providers)



@app.route('/api/services', methods=['GET'])
def get_services():
    query = (Services
             .select(Services, fn.COUNT(fn.DISTINCT(Visit_Record.NeighborID)).alias('TotalNeighbors'))
             .join(Visit_Service)
             .join(Visit_Record)
             .group_by(Services))

    services = []
    for service in query:
        service_dict = service.to_dict()
        # Add the TotalNeighbors count to the dictionary that is being sent to frontend
        service_dict['TotalNeighbors'] = service.TotalNeighbors
        services.append(service_dict)

    return jsonify(services)



@app.route('/api/inventory_usageAD', methods=['GET'])
def get_inventory_usageAD():
    query = (Inventory
             .select(Inventory, Inventory_Usage, Visit_Record.Date.alias('VisitDate'))
             .join(Inventory_Usage, on=(Inventory.InventoryID == Inventory_Usage.Inventory_UseID))
             .join(Visit_Record, on=(Inventory_Usage.RecordID == Visit_Record.RecordID)))

    inventory_usage_data = []
    for inventory_item in query:
        item_dict = inventory_item.to_dict()
        item_dict['VisitDate'] = inventory_item.VisitDate.strftime('%Y-%m-%d')
        inventory_usage_data.append(item_dict)

    return jsonify(inventory_usage_data)




# @app.route('/api/neighbors', methods=['GET'])
# def get_neighbors():
#     query = Neighbor.select()
#     neighbors = [neighbor.to_dict() for neighbor in query]
#     return jsonify(neighbors)

@app.route('/api/visit_records', methods=['GET'])
def get_visit_records():
    query = Visit_Record.select()
    visit_records = [record.to_dict() for record in query]
    return jsonify(visit_records)

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    query = Inventory.select()
    inventory = [item.to_dict() for item in query]
    return jsonify(inventory)

@app.route('/api/inventory_usage', methods=['GET'])
def get_inventory_usage():
    query = Inventory_Usage.select()
    inventory_usage = [usage.to_dict() for usage in query]
    return jsonify(inventory_usage)



@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Response from root - Home page - This is being sent by backend /"})

# 1. Identify all volunteers who are allowed to access records:
@app.route('/api/volunteers/record_access', methods=['GET'])
def get_volunteers_with_record_access():
    query = Volunteer.select().where(Volunteer.HasRecordAccess == True)
    volunteers = [volunteer.to_dict() for volunteer in query]
    return jsonify(volunteers)

if __name__ == '__main__':
    app.run(debug=True)


# Rest of the queries.


# 1. Identify all volunteers who are allowed to access records:
@app.route('/api/volunteers/record_access', methods=['GET'])
def get_volunteers_with_record_access():
    query = Volunteer.select().where(Volunteer.HasRecordAccess == True)
    volunteers = [volunteer.to_dict() for volunteer in query]
    return jsonify(volunteers)

# 2. Find all the records of visits made to a particular neighbor
@app.route('/api/visit_records/<int:neighbor_id>', methods=['GET'])
def get_visit_records_for_neighbor(neighbor_id):
    query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
    visit_records = [record.to_dict() for record in query]
    return jsonify(visit_records)

# 3. Get a list of visit records along with the names of neighbors visited and the volunteer who made the visit
@app.route('/api/visit_records/details', methods=['GET'])
def get_visit_records_details():
    query = (Visit_Record
             .select(Visit_Record, Neighbor, Volunteer)
             .join(Neighbor)
             .join(Volunteer))
    visit_records = [{
        'Date': record.Date,
        'Neighbor': f"{record.neighbor.FirstName} {record.neighbor.LastName}",
        'Volunteer': f"{record.volunteer.FirstName} {record.volunteer.LastName}"
    } for record in query]
    return jsonify(visit_records)

# 4. Count the number of times each service has been provided
@app.route('/api/services/count', methods=['GET'])
def get_service_counts():
    query = (Visit_Service
             .select(Visit_Service.ServiceID, fn.Count(Visit_Service.ServiceOrder).alias('Count'))
             .group_by(Visit_Service.ServiceID))
    service_counts = [{
        'ServiceID': service.ServiceID,
        'Count': service.Count
    } for service in query]
    return jsonify(service_counts)

# 5. Get a list of items in the inventory that will expire within a specified period
@app.route('/api/inventory/expiring', methods=['GET'])
def get_expiring_inventory():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = Inventory.select().where((Inventory.ExpirationDate >= start_date) & (Inventory.ExpirationDate <= end_date))
    expiring_inventory = [item.to_dict() for item in query]
    return jsonify(expiring_inventory)

# 6. Count the number of neighbors who have pets
@app.route('/api/neighbors/pets_count', methods=['GET'])
def get_neighbors_with_pets_count():
    pet_count = Neighbor.select().where(Neighbor.HasPet == True).count()
    return jsonify({'PetCount': pet_count})

# 7. Find all visit records conducted on a specific date
@app.route('/api/visit_records/date/<date:date_string>', methods=['GET'])
def get_visit_records_on_date(date_string):
    target_date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    query = Visit_Record.select().where(Visit_Record.Date == target_date)
    visit_records = [record.to_dict() for record in query]
    return jsonify(visit_records)

# 8.Get list of services provided by a specific organization every year
@app.route('/api/services/provider/<string:provider_id>/year/<int:year>', methods=['GET'])
def get_services_by_provider_year(provider_id, year):
    query = (Services
             .select(Services, fn.COUNT(Visit_Record.RecordID).alias('ServiceCount'))
             .join(Visit_Service)
             .join(Visit_Record)
             .where((Services.OrganizationID == provider_id) & (fn.EXTRACT('year', Visit_Record.Date) == year))
             .group_by(Services))
    services_by_year = [{
        'ServiceID': service.ServiceID,
        'ServiceType': service.ServiceType,
        'ServiceCount': service.ServiceCount
    } for service in query]
    return jsonify(services_by_year)

# 9. Get list of organization providing service with the list of service they each provide
@app.route('/api/providers/services', methods=['GET'])
def get_providers_with_services():
    query = Service_Providers.select()
    providers_with_services = []
    for provider in query:
        provider_data = provider.to_dict()
        provider_data['Services'] = [service.ServiceType for service in provider.services]
        providers_with_services.append(provider_data)
    return jsonify(providers_with_services)

#10 Get all visit records for a specific neighbor 
@app.route('/api/visit_records/<int:neighbor_id>', methods=['GET'])
def get_visit_records_for_neighbor(neighbor_id):
    query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
    visit_records = [record.to_dict() for record in query]
    return jsonify(visit_records)



#11 Get neighbor details along with their visit records, services, and volunteers associated with those visit records. 
@app.route('/api/neighbor/<int:neighbor_id>', methods=['GET'])
def get_neighbor_details(neighbor_id):
    try:
        
        neighbor = Neighbor.get_by_id(neighbor_id)
        neighbor_info = {
            'NeighborID': neighbor.NeighborID,
            'FullName': f"{neighbor.FirstName} {neighbor.LastName}",
            'DateOfBirth': neighbor.DateOfBirth.strftime('%Y-%m-%d')  # Format date of birth
            
        }

        
        visit_records_query = Visit_Record.select().where(Visit_Record.NeighborID == neighbor_id)
        visit_records = []

        
        for record in visit_records_query:
            visit_info = {
                'VisitID': record.VisitID,
                'Date': record.Date.strftime('%Y-%m-%d'),  # Format visit date
                
            }

            
            services_query = Visit_Service.select().where(Visit_Service.RecordID == record.RecordID)
            services_info = [service.ServiceType for service in services_query]
            visit_info['Services'] = services_info

            
            volunteers_query = Volunteer.select().join(Visit_Record).where(Visit_Record.RecordID == record.RecordID)
            volunteers_info = [{
                'VolunteerID': volunteer.VolunteerID,
                'FullName': f"{volunteer.FirstName} {volunteer.LastName}"
            } for volunteer in volunteers_query]
            visit_info['Volunteers'] = volunteers_info

            
            visit_records.append(visit_info)

        
        return jsonify({
            'NeighborInfo': neighbor_info,
            'VisitRecords': visit_records
        }), 200

    except Neighbor.DoesNotExist:
        return jsonify({'error': 'Neighbor not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 12. Get all visits conducted within a specified date range
@app.route('/api/visit_records/range', methods=['GET'])
def get_visits_in_date_range():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = Visit_Record.select().where((Visit_Record.Date >= start_date) & (Visit_Record.Date <= end_date))
    visits = [visit.to_dict() for visit in query]
    return jsonify(visits)

# 13. Get all neighbors who have not received any visits
@app.route('/api/neighbors/no_visits', methods=['GET'])
def get_neighbors_without_visits():
    query = Neighbor.select().where(~(Neighbor.neighbor_records.exists()))
    neighbors = [neighbor.to_dict() for neighbor in query]
    return jsonify(neighbors)

# 14. Get list of organization providing service with the list of service they each provide
@app.route('/api/providers/services', methods=['GET'])
def get_providers_with_services():
    query = Service_Providers.select()
    providers_with_services = []
    for provider in query:
        provider_data = provider.to_dict()
        provider_data['Services'] = [service.ServiceType for service in provider.services]
        providers_with_services.append(provider_data)
    return jsonify(providers_with_services)

# 15.Get all volunteers who have provided a specific service
@app.route('/api/services/<int:service_id>/volunteers', methods=['GET'])
def get_volunteers_for_service(service_id):
    query = (Volunteer
             .select(Volunteer)
             .join(Visit_Record)
             .join(Visit_Service)
             .where(Visit_Service.ServiceID == service_id))
    volunteers = [volunteer.to_dict() for volunteer in query]
    return jsonify(volunteers)

# 16. Get all visits conducted by a specific volunteer
@app.route('/api/volunteers/<int:volunteer_id>/visits', methods=['GET'])
def get_visits_by_volunteer(volunteer_id):
    query = (Visit_Record
             .select()
             .join(Volunteer)
             .where(Volunteer.VolunteerID == volunteer_id))
    visits = [visit.to_dict() for visit in query]
    return jsonify(visits)



# @app.route('/api/services', methods=['GET'])
# def get_services():
#     query = Services.select()
#     services = [service.to_dict() for service in query]
#     return jsonify(services)

# @app.route('/api/services', methods=['GET'])
# def get_services():
#     query = Services.select()
#     services = [service.to_dict() for service in query]
#     return jsonify(services)

#Below is example api call to get the neighbors from passing in, but with mock neighbors instead of real data
# @app.route('/NeighborTableAdd', methods=['GET'])
# def neighbor():
#     # Mock neighbor object
#     mock_neighbor = {
#         "NeighborID": 1,
#         "VolunteerID": 101,  # Assuming a volunteer ID; replace with relevant data
#         "Organization": "Helping Hands",
#         "FirstName": "John",
#         "LastName": "Doe",
#         "DateOfBirth": "1990-01-01",
#         "Phone": "555-1234",
#         "Location": "123 Main St, Anytown, USA",
#         "Email": "johndoe@example.com",
#         "Created_date": datetime.datetime.now().isoformat(),
#         "HasStateID": True,
#         "HasPet": False
#     }
#     mock_neighborTwo = {
#         "NeighborID": 2,
#         "VolunteerID": 102,  # Assuming a volunteer ID; replace with relevant data
#         "Organization:": "Helping Hands",
#         "FirstName": "Jane",
#         "LastName": "Doe",
#         "DateOfBirth": "1990-01-01",
#         "Phone": "555-1234",
#         "Location": "123 Main St, Anytown, USA",
#         "Email": "janedoe@example.com",
#         "Created_date": datetime.datetime.now().isoformat(),
#         "HasStateID": True,
#         "HasPet": False
#     }
#     return mock_neighbor, mock_neighborTwo
    
    # def neighbors():
    # neighbors = neighbor()
    # return jsonify(neighbors)
