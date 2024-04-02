from flask import Flask, request, redirect, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from models import *
from logic import * 

#to run type flask run in the terminal
app = Flask(__name__)

## additions Nicholas
# starting point for Flask web application that interacts with PostgreSQL database.

# Application's Routes:
# Home/Dashboard Page (/): Display a dashboard or list of entries.
# Add Entry Page (/add): Show a form to input new records.
# Add Entry Action (/add - POST): Handle the form submission for adding new records.
# View Entry (/entry/<id>): Display details for a specific entry.
# Delete Entry (/delete/<id> - POST): Delete a specific entry. We use POST to safely delete data.

#Root URL
@app.route('/')
def index():
    # Example: Fetch all entries. Adjust according to your actual model.
    entries = Volunteer.select()  # Adjust Volunteer to your model
    return render_template('index.html', entries=entries)

# Route for user registration, here starts the creation of the profile 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        hashed_password = generate_password_hash(password)

        try:
            Volunteer.create(VolunteerID = username, Email=email, Password=hashed_password, Phone = phone)
            return redirect(url_for('login'))
        except IntegrityError:
            # Handle duplicate username or email
            return render_template('register.html', error='Username or email already exists')
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        username = Volunteer.get_or_none(VolunteerID = username)
        if username and check_password_hash(Volunteer.password, password):
            session['username'] = Volunteer.VolunteerID
            return redirect(url_for('profile'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

# Route for user logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index.html'))

# Route for adding a neighboor
@app.route('/add', methods=['POST'])
def add_Neighbor():
    if request.method == ['POST']:
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        Organization = request.form['Organization']
        Email = request.form['Email']
        DateOfBirth = request.form['DateofBirth']
        Phone = request.form['Phone']
        Address = request.form['Address']
        
        HasPet = request.form.get('HasPet')
        if HasPet.lower() not in ['yes', 'no']:
            return render_template('form.html', error='Please enter "True" or "False" for the boolean input')
        
        HasStateID = request.form.get('StateID')
        if HasStateID.lower() not in ['yes', 'no']:
            return render_template('form.html', error='Please enter "True" or "False" for the boolean input')

        try:
            Neighbor.create(FirstName = FirstName, LastName = LastName, Organization = Organization, Email = Email,
                            DateOfBirth = DateOfBirth, Phone = Phone, Address = Address,
                            HasPet = HasPet, HasStateID = HasStateID)
            return redirect(url_for('add_neighbor.html'))
        except IntegrityError:
            # Handle duplicate username or email
            return render_template('add_neighbor.html', error='Neighbor already exists')
    return "Form submitted successfully!"

@app.route('/entry/<int:id>')
def view_entry(id):
    # Fetch a specific entry by ID. Adjust according to your actual model.
    entry = Volunteer.get(Volunteer.id == id)  # Adjust Volunteer to your model
    return render_template('view_entry.html', entry=entry)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    # Delete a specific entry. Ensure safety by using POST.
    entry = Volunteer.get(Volunteer.id == id)  # Adjust Volunteer to your model
    entry.delete_instance()
    return redirect(url_for('home'))

## additions Nicholas
# Service Providers Example ########################################
@app.route('/service-providers')
def list_service_providers():
    service_providers = get_all_service_providers()
    return render_template('list_service_providers.html', service_providers=service_providers)

@app.route('/service-providers/add', methods=['GET', 'POST'])
def add_service_provider_route():
    if request.method == 'POST':
        org_name = request.form['organization']
        contact = request.form['contactPerson']
        email = request.form['email']
        phone = request.form['phone']
        date_of_start = request.form['dateOfStart']
        add_service_provider(org_name, contact, email, phone, date_of_start)
        return redirect(url_for('list_service_providers'))
    return render_template('add_service_provider.html')

@app.route('/service-providers/<organization>')
def view_service_provider(organization):
    provider = get_service_provider(organization)
    return render_template('view_service_provider.html', provider=provider)

if __name__ == "__main__":
    app.run(debug=True) # so that if we have any errors we can see it in the web page
