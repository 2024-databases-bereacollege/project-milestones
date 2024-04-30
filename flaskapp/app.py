from flask import Flask, request, redirect, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from models import *


#to run type flask run in the terminal
app = Flask(__name__)

# Root URL
@app.route('/')
def index():
    # Example: Fetch all entries. Adjust according to your actual model.
    entries = Volunteer.select()  # Adjust Volunteer to your model
    return render_template('index.html', entries=entries)

# Route for user registration, for creating a new profile
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)

        try:
            # Create a new volunteer profile
            Volunteer.create(VolunteerID=username, Email=email, Password=hashed_password, Phone=phone)
            return redirect(url_for('login.html'))  # Redirect to login page after successful registration
        except IntegrityError:
            # Handle duplicate username or email
            return render_template('register.html', error='Username or email already exists')
    return render_template('register.html')  # Render the registration form

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract username and password from the login form
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the database and if the password is correct
        user = Volunteer.get_or_none(VolunteerID=username)
        if user and check_password_hash(user.password, password):
            # Set the user's username in the session to track their login status
            session['username'] = user.VolunteerID
            return redirect(url_for('index.html'))  # Redirect to the home page after successful login
        else:
            # Display an error message if the login credentials are invalid
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')  # Render the login form

# Route for user logout
@app.route('/logout')
def logout():
    # Clear the session to log the user out
    session.clear()
    return redirect(url_for('login.html'))  # Redirect to the login page after logout




@app.route('/volunteer', methods=['GET'])
def get_volunteer():
    volunteer = [volunteer.to_dict() for volunteer in Volunteer.select()]
    return jsonify(volunteer)

@app.route('/volunteers/add', methods=['POST'])
def add_volunteer():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password)

        # Check if the volunteer already exists in the database
        existing_volunteer = Volunteer.get_or_none(Email=email)
        if existing_volunteer:
            # Update existing volunteer's information
            existing_volunteer.VolunteerID = username
            existing_volunteer.Password = hashed_password
            existing_volunteer.Phone = phone
            existing_volunteer.save()  # Save the changes to the database
            return jsonify(existing_volunteer.to_dict())
        else:
            # Create a new volunteer
            new_volunteer = Volunteer.create(
                VolunteerID=username,
                Email=email,
                Password=hashed_password,
                Phone=phone
            )
            return jsonify(new_volunteer.to_dict())



@app.route('/neighbors', methods=['GET'])
def neighbor():
    neighbors = Neighbor.query.all()
    return render_template('neighbor.html', neighbors=neighbors)

# Route for adding/editing a neighbor
@app.route('/neighbors/add', methods=['POST'])
def add_neighbor():
    if request.method == 'POST':
        neighbor_id = request.form.get('NeighborID')
        edit = request.args.get('edit') == 'true'
        
        if neighbor_id and edit:
            # Editing existing neighbor
            neighbor = Neighbor.query.get(neighbor_id)
            if neighbor:
                # Update neighbor's details based on the form data
                neighbor.FirstName = request.form['FirstName']
                neighbor.LastName = request.form['LastName']
                neighbor.Organization = request.form['Organization']
                neighbor.Email = request.form['Email']
                neighbor.DateOfBirth = datetime.datetime.strptime(request.form['DateOfBirth'], '%Y-%m-%d')
                neighbor.Phone = request.form['Phone']
                neighbor.Location = request.form['Location']
                neighbor.HasPet = request.form.get('HasPet')
                neighbor.HasStateID = request.form.get('HasStateID')
                mydb.session.commit()  # Save the changes to the database
                return redirect(url_for('neighbor.html'))  # Redirect to the neighbor list page
            else:
                return render_template('error.html', message='Neighbor not found')
        else:
            # Adding a new neighbor
            new_neighbor = Neighbor(
                FirstName=request.form['FirstName'],
                LastName=request.form['LastName'],
                Organization=request.form['Organization'],
                Email=request.form['Email'],
                DateOfBirth=datetime.datetime.strptime(request.form['DateOfBirth'], '%Y-%m-%d'),
                Phone=request.form['Phone'],
                Location=request.form['Location'],
                HasPet=request.form.get('HasPet'),
                HasStateID=request.form.get('HasStateID')
            )
            mydb.session.add(new_neighbor)  # Add the new neighbor to the database
            mydb.session.commit()  # Commit the transaction
            return redirect(url_for('neighbor_list'))  # Redirect to the neighbor list page
    else:
        # Render the form for adding/editing a neighbor
        neighbor_id = request.args.get('NeighborID')
        edit = request.args.get('edit') == 'true'
        
        if neighbor_id and edit:
            # Fetch the neighbor to be edited and render the edit form
            neighbor = Neighbor.query.get(neighbor_id)
            if neighbor:
                return render_template('edit_neighbor.html', neighbor=neighbor)
            else:
                return render_template('error.html', message='Neighbor not found')
        return render_template('add_neighbor.html')

# Route for displaying all service providers
@app.route('/providers', methods=['GET'])
def service_providers():
    providers = Service_Providers.query.all()
    return render_template('providers.html', providers=providers)

# Route for adding/editing a service provider
@app.route('/providers/add', methods=['POST'])
def add_service_provider():
    if request.method == 'POST':
        organization_id = request.form.get('Organization')
        edit = request.args.get('edit') == 'true'
        
        if organization_id and edit:
            # Editing existing service provider
            organization = Service_Providers.query.get(organization_id)
            if organization:
                # Update organization's details based on the form data
                organization.ContactPerson = request.form['ContactPerson']
                organization.Email = request.form['Email']
                organization.Phone = request.form['Phone']
                organization.DateOfStart = datetime.datetime.strptime(request.form['DateOfStart'], '%Y-%m-%d')
                mydb.session.commit()  # Save the changes to the database
                return redirect(url_for('service_providers'))  # Redirect to the service providers list page
            else:
                return render_template('error.html', message='Service Provider not found')
        else:
            # Adding a new service provider
            new_provider = Service_Providers(
                Organization=request.form['Organization'],
                ContactPerson=request.form['ContactPerson'],
                Email=request.form['Email'],
                Phone=request.form['Phone'],
                DateOfStart=datetime.datetime.strptime(request.form['DateOfStart'], '%Y-%m-%d')
            )
            mydb.session.add(new_provider)  # Add the new service provider to the database
            mydb.session.commit()  # Commit the transaction
            return render_template('home.html', message='Service Provider created')  # Redirect to home page with success message
        
    else:
        # Render the form for adding/editing a service provider
        organization_id = request.args.get('organization_name')
        edit = request.args.get('edit') == 'true'
        
        if organization_id and edit:
            # Fetch the service provider to be edited and render the edit form
            organization = Service_Providers.query.get(organization_id)
            if organization:
                return render_template('edit_service_provider.html', organization=organization)
            else:
                return render_template('home.html', message='Service Provider not found')
        return render_template('add_service_provider.html')

# Route for displaying all services
@app.route('/services', methods=['GET'])
def services():
    services = Services.select()
    return render_template('services.html', services=services)

# Route for adding/editing a service
@app.route('/services/add', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        service_id = request.form.get('ServiceID')
        edit = request.args.get('edit') == 'true'
        
        if service_id and edit:
            # Editing existing service
            service = Services.get_or_none(id=service_id)
            if service:
                # Update service's details based on the form data
                service.ServiceType = request.form['ServiceType']
                service.Organization = request.form['Organization']
                mydb.session.commit()  # Save the changes to the database
                return redirect(url_for('services.html'))  # Redirect to the services list page
            else:
                return render_template('error.html', message='Service not found')
        else:
            # Adding a new service
            new_service = Services(
                ServiceType=request.form['ServiceType'],
                Organization=request.form['Organization']
            )
            mydb.session.add(new_service)  # Add the new service to the database
            mydb.session.commit()  # Commit the transaction
            return redirect(url_for('services.html'))  # Redirect to the services list page
    else:
        # Render the form for adding/editing a service
        service_id = request.args.get('ServiceID')
        edit = request.args.get('edit') == 'true'
        
        if service_id and edit:
            # Fetch the service to be edited and render the edit form
            service = Services.get_or_none(id=service_id)
            if service:
                return render_template('edit_service.html', service=service)
            else:
                return render_template('error.html', message='Service not found')
        return render_template('add_service.html')

# Route for displaying all visits
@app.route('/visits', methods=['GET'])
def visits():
    visits = Visit_Service.select()
    return render_template('visits.html', visits=visits)

# Route for adding/editing a visit service
@app.route('/visits/add', methods=['GET', 'POST'])
def add_edit_visit_service():
    if request.method == 'POST':
        # Extract form data
        description = request.form['Description']
        # Check if it's an edit operation
        edit = request.args.get('edit') == 'true'
        if edit:
            # Editing existing visit service
            service_order = request.form['ServiceOrder']
            visit_service = Visit_Service.get_or_none(ServiceOrder=service_order)

            if visit_service:
                # Update only the description field, foreign key fields remain unchanged
                visit_service.Description = description
                mydb.session.commit()  # Save the changes to the database
                return redirect(url_for('visits'))  # Redirect to the visits list page
            else:
                return render_template('error.html', message='Visit service not found')
        else:
            # Adding new visit service
            new_visit_service = Visit_Service(
                Description=description
            )
            mydb.session.add(new_visit_service)  # Add the new visit service to the database
            mydb.session.commit()  # Commit the transaction
            return redirect(url_for('visits'))  # Redirect to the visits list page
    else:
        # Render the form for adding/editing a visit service
        return render_template('add_visit_service.html')

# Route for displaying all visit records
@app.route('/records', methods=['GET'])
def records():
    records = Visit_Record.select()
    return render_template('records.html', records=records)

# Route for adding/editing a visit record
@app.route('/records/add', methods=['GET', 'POST'])
def add_edit_record():
    if request.method == 'POST':
        # Extract form data
        date = request.form['Date']
        time = request.form['Time']
        notes = request.form['Notes']
        service_order_id = request.form['ServiceOrderID']

        # Check if it's an edit operation
        edit = request.args.get('edit') == 'true'

        if edit:
            # Editing existing visit record
            record_id = request.form['RecordID']
            visit_record = Visit_Record.get_or_none(RecordID=record_id)

            if visit_record:
                # Update only the date, time, and notes fields, foreign key fields remain unchanged
                visit_record.Date = date
                visit_record.Time = time
                visit_record.Notes = notes
                mydb.session.commit()  # Save the changes to the database
                return redirect(url_for('records'))  # Redirect to the records list page
            else:
                return render_template('error.html', message='Visit record not found')
        else:
            # Adding new visit record
            new_visit_record = Visit_Record(
                Date=date,
                Time=time,
                Notes=notes,
                ServiceOrderID=service_order_id
            )
            mydb.session.add(new_visit_record)  # Add the new visit record to the database
            mydb.session.commit()  # Commit the transaction
            return redirect(url_for('records'))  # Redirect to the records list page
    else:
        # Render the form for adding/editing a visit record
        return render_template('add_record.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
