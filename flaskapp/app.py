from flask import Flask, request, redirect, render_template, url_for

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

@app.route('/')
def home():
    # Example: Fetch all entries. Adjust according to your actual model.
    entries = Volunteer.select()  # Adjust Volunteer to your model
    return render_template('home.html', entries=entries)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        # Process form data and add new entry. Adjust according to your model and form fields.
        # Example:
        # new_entry = Volunteer.create(firstname=request.form['firstname'], lastname=request.form['lastname'])
        # return redirect(url_for('home'))
        pass  # Remove this once you add the form handling code
    return render_template('add_entry.html')  # Show the form

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
#####################################################################
