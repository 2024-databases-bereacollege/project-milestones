from flask import Flask, request, redirect, render_template, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from flask_cors import CORS #to allow the front end to communicate with the back end
from models import *
from logic import * 

#to run type flask run in the terminal or type the other
app = Flask(__name__)

CORS(app)
#CORS(app, resources={r"/*":{'origins':"*"}}) #TODO fix before deploying -to allow the front end to communicate with the back end - allowing all origins

@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/NeighborTable', methods=['GET'])
def neighbor():
    # Mock neighbor object
    mock_neighbor = {
        "NeighborID": 1,
        "VolunteerID": 101,  # Assuming a volunteer ID; replace with relevant data
        "Organization": "Helping Hands",
        "FirstName": "John",
        "LastName": "Doe",
        "DateOfBirth": "1990-01-01",
        "Phone": "555-1234",
        "Address": "123 Main St, Anytown, USA",
        "Email": "johndoe@example.com",
        "Created_date": datetime.datetime.now().isoformat(),
        "HasStateID": True,
        "HasPet": False
    }
    return jsonify(mock_neighbor)

if __name__ == '__main__':
    app.run(debug=True)
