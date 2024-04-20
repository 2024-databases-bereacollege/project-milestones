"""
This is the main file for your Flask app, containing app set-up and all of the routes.
In a more complex application you would split your routes into other files as needed.
"""
from datetime import datetime

from flask import jsonify


from flask import Flask, render_template, request
from peewee import IntegrityError
from models import mydb, chapter, member, event, donation
from flask_wtf import CSRFProtect
from flask import redirect
from flask import url_for


# from logic import *

app = Flask(__name__)

@app.before_request
def before_request():
    mydb.connect()

@app.after_request
def after_request(response):
    mydb.close()
    return response

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db/data'


@app.route('/')
def admin_panel():
    # courses = Course.select()
    return render_template("index.html")

@app.route('/members')
def members():
    members = member.select()
    return render_template("members.html", members=members)

@app.route('/main')
def main_page():
    # Using Peewee to query all chapters
    chapters = chapter.select()
    return render_template("main.html", chapters=chapters)


@app.route('/events')
def events():
    event_data = event.select()
    return render_template("events.html", events=event_data)
   
@app.route('/donations')
def donations():
    donations_query = donation.select().join(member)
    print(donations_query)
    return render_template("donations.html", donations=donations_query)



@app.route('/add_member', methods=['POST'])
def add_member():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        last_name = request.form.get('last_name')
        phone_number = request.form.get('phone_number')
        score = request.form.get('score')
        address = request.form.get('address')
        number_of_events_attended = request.form.get('number_of_events_attended')

        try:
            new_member = member.create(
                firstname=first_name,
                middlename=middle_name,
                lastname=last_name,
                phonenumber=phone_number,
                score=score,
                memberaddress=address,
                numberofeventsattended=int(number_of_events_attended)
            )
            new_member.save()

            return redirect(url_for('members'))
        except Exception as e:
            # Here, consider adding error logging or handling
            print(f"An error occurred: {e}")
            # Optionally, return an error message or status
            return "An error occurred", 500

    
@app.route('/add_event', methods=['POST'])
def add_event():
    try:
        new_event = event.create(
            eventname=request.form['event_name'],
            venue=request.form['venue'],
            eventdate=request.form['event_date'],
            theme=request.form['theme'],
            numberofmembersattended=request.form['attendance']
        )
        new_event.save()
        return redirect(url_for('events'))
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred", 500

@app.route('/add_donation', methods=['POST'])
def add_donation():
    try:
        new_donation = donation.create(
            donor=request.form['donor_id'],
            item=request.form['item'],
            monetaryWorth=request.form['monetaryWorth']
        )
        new_donation.save()
        return redirect(url_for('donations'))
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred", 500
    
    return jsonify({"success": True, "message": "Donation added successfully"})




"""
Flask can use a variety of decorators to enhance application functionality.
In this case we are using `before_request` to add code that executes before
every request to the application. 

This method gets a user from the database and assigns it to an attribute of 
Flask's global object, `g`.  `g` is available in all templates, and is defined
for the duration of the request. Note: `g` does NOT persist between different 
requests. Sessions, cookies, and the database must be used for true persistence.

Obviously, hard-coding one particular student as the logged-in user is not what
a real application would do. In practice, this function would get a user from 
whatever the login/authentication system has stored in the session.
"""
# from flask import g
# @app.before_request
# def load_user():
#     g.user = Student.get_by_id(2)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)