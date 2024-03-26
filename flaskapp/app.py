from flask import Flask, request, redirect, render_template, url_for

from models import *
#from logic import *

#to run type flask run in the terminal
app = Flask(__name__)

## additions Nicholas

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
