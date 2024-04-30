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





# @app.route('/api/services', methods=['GET'])
# def get_services():
#     query = Services.select()
#     services = [service.to_dict() for service in query]
#     return jsonify(services)






@app.route('/api/neighbors', methods=['GET'])
def get_neighbors():
    query = Neighbor.select()
    neighbors = [neighbor.to_dict() for neighbor in query]
    return jsonify(neighbors)

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


if __name__ == '__main__':
    app.run(debug=True)










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
