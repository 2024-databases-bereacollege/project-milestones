from flask import Flask, request, redirect, render_template, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash #Using for passwords 
from models import *
from logic import * 

#to run type flask run in the terminal
app = Flask(__name__)

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
    return redirect(url_for('login.html'))

# Route for adding a neighboor
@app.route('/add', methods=['POST'])
def add_neighbor():
    if request.method == 'POST':
        neighbor_id = request.form.get('NeighborID')
        edit = request.args.get('edit') == 'true'
        
        if neighbor_id and edit:
            neighbor = Neighbor.query.get(neighbor_id)
            if neighbor:
                neighbor.FirstName = request.form['FirstName']
                neighbor.LastName = request.form['LastName']
                neighbor.Organization = request.form['Organization']
                neighbor.Email = request.form['Email']
                neighbor.DateOfBirth = datetime.datetime.strptime(request.form['DateOfBirth'], '%Y-%m-%d')
                neighbor.Phone = request.form['Phone']
                neighbor.Address = request.form['Address']
                neighbor.HasPet = request.form.get('HasPet')
                neighbor.HasStateID = request.form.get('HasStateID')
                mydb.session.commit()
                return redirect(url_for('neighbor_list'))
            else:
                return render_template('error.html', message='Neighbor not found')
        else:
            new_neighbor = Neighbor(
                FirstName=request.form['FirstName'],
                LastName=request.form['LastName'],
                Organization=request.form['Organization'],
                Email=request.form['Email'],
                DateOfBirth=datetime.datetime.strptime(request.form['DateOfBirth'], '%Y-%m-%d'),
                Phone=request.form['Phone'],
                Address=request.form['Address'],
                HasPet=request.form.get('HasPet'),
                HasStateID=request.form.get('HasStateID')
            )
            mydb.session.add(new_neighbor)
            mydb.session.commit()
            return redirect(url_for('neighbor_list'))
    else:
        neighbor_id = request.args.get('NeighborID')
        edit = request.args.get('edit') == 'true'
        
        if neighbor_id and edit:
            neighbor = Neighbor.query.get(neighbor_id)
            if neighbor:
                return render_template('edit_neighbor.html', neighbor=neighbor)
            else:
                return render_template('error.html', message='Neighbor not found')
        return render_template('create_neighbor.html')
    
@app.route('/add', methods=['POST'])
def Provider_Services():
    if request.method == 'POST':
        organization_id = request.form.get('Organization')
        edit = request.args.get('edit') == 'true'
        
        if organization_id and edit:
            organization = Service_Providers.query.get(organization_id)
            if organization:
                organization.ContactPerson = request.form['ContactPerson']
                organization.Email = request.form['Email']                
                organization.Phone = request.form['Phone']
                organization.DateOfStart = datetime.datetime.strptime(request.form['DateOfStart'], '%Y-%m-%d')
                mydb.session.commit()
                return redirect(url_for('service_providers'))  # Redirect to service_providers or another page
            else:
                return render_template('error.html', message='Service Provider not found')
        else:
            new_service = Service_Providers(
                Organization=request.form['Organization'],
                ContactPerson=request.form['ContactPerson'],
                Email=request.form['Email'],
                Phone=request.form['Phone'],
                DateOfStart=datetime.datetime.strptime(request.form['DateOfStart'], '%Y-%m-%d')
            )
            mydb.session.add(new_service)
            mydb.session.commit()
            return render_template('home.htm', message='Service Provider created')
        
    else:
        organization_id = request.args.get('organization_name')
        edit = request.args.get('edit') == 'true'
        
        if organization_id and edit:
            organization = Service_Providers.query.get(organization_id)
            if organization:
                return render_template('edit_service_provider.html', organization=organization)
            else:
                return render_template('home.html', message='Service Provider not found')
        return render_template('Service_Provider.html')
    
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
