from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *



app = Flask(__name__)

app.config.from_object(__name__)
CORS(app)
#CORS(app, resources={r"/*":{'origins':"*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080',"allow_headers": "Access-Control-Allow-Origin"}})

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
    print("Received data for update:", data)  # Debugging to see what data is received

    for key, value in data.items():
        if hasattr(volunteer, key):  # Ensure the attribute exists before setting it
            setattr(volunteer, key, value)

    myappdb.session.commit()  # Make sure this is the correct session object name
    return jsonify(volunteer.to_dict()), 200


@app.route('/api/volunteers', methods=['DELETE']) #DELETE request to delete a volunteer
def delete_volunteer(id):
    volunteer = Volunteer.query.get(id)
    if not volunteer:
        return jsonify({'error': 'Volunteer not found'}), 404

    myappdb.session.delete(volunteer)
    myappdb.session.commit()
    return jsonify({'success': 'Volunteer deleted'}), 200

@app.route('/api/volunteers', methods=['POST']) #POST request to add a volunteer
def add_volunteer():
    try:
        data = request.get_json()  # Get data sent from the frontend

        # Ensure all required fields are in the data
        if not all(key in data for key in ['FirstName', 'LastName', 'Password', 'Email', 'Phone', 'HasRecordAccess']):
            return jsonify({"error": "Missing data for one or more fields"}), 400

        # Create a new Volunteer instance with hashed password
        volunteer = Volunteer(
            first_name=data['FirstName'],
            last_name=data['LastName'],
            password=generate_password_hash(data['Password']),  # Hash the password for security
            email=data['Email'],
            phone=data['Phone'],
            has_record_access=data['HasRecordAccess']
        )
        myappdb.session.add(volunteer)  # Add new volunteer to the session
        myappdb.session.commit()  # Commit the session to save the volunteer to the database

        return jsonify(volunteer.to_dict()), 201  # Return the created volunteer and a 201 CREATED status
    except Exception as e:
        myappdb.session.rollback()  # Roll back the session in case of error
        return jsonify({"error": str(e)}), 400  # Return error message if something goes wrong


@app.route('/api/service_providers', methods=['GET'])
def get_service_providers():
    query = Service_Providers.select()
    service_providers = [provider.to_dict() for provider in query]
    return jsonify(service_providers)

@app.route('/api/services', methods=['GET'])
def get_services():
    query = Services.select()
    services = [service.to_dict() for service in query]
    return jsonify(services)

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
#         "Address": "123 Main St, Anytown, USA",
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
#         "Address": "123 Main St, Anytown, USA",
#         "Email": "janedoe@example.com",
#         "Created_date": datetime.datetime.now().isoformat(),
#         "HasStateID": True,
#         "HasPet": False
#     }
#     return mock_neighbor, mock_neighborTwo
    
    # def neighbors():
    # neighbors = neighbor()
    # return jsonify(neighbors)
