from datetime import datetime
from flask import Flask, jsonify, render_template, request, redirect, url_for
from peewee import IntegrityError
from models import mydb, chapter, member, event, donation, event_attendance
app = Flask(__name__)
@app.before_request
def before_request():
    # Ensure database connection is established at the start of each request
    mydb.connect()
@app.after_request
def after_request(response):
    # Ensure database connection is closed after each request
    mydb.close()
    return response
@app.route('/')
def admin_panel():
    # Render the main admin panel page
    return render_template("index.html")
@app.route('/members')
def members():
    # Fetch all members and render them in the 'members.html'
    members_query = member.select()
    members_list = [member_to_dict(m) for m in members_query]
    return render_template("members.html", members=members_list)
@app.route('/main')
def main_page():
    # Handle sorting of chapters
    sort_by = request.args.get('sort_by', 'chaptername-asc')
    try:
        field, order = sort_by.split('-')
        order_method = chapter.chaptername.desc() if order == 'desc' else chapter.chaptername.asc()
    except ValueError:
        field, order_method = 'chaptername', chapter.chaptername.asc()
    if field == 'numberofmembers':
        order_method = chapter.numberofmembers.desc() if order == 'desc' else chapter.numberofmembers.asc()
    chapters_query = chapter.select().order_by(order_method)
    chapters = [{
        'chaptername': c.chaptername,
        'numberofmembers': c.numberofmembers,
        'chapterlead': c.chapterlead,
        'chapteremail': c.chapteremail
    } for c in chapters_query]
    return render_template("main.html", chapters=chapters)
@app.route('/update_chapter', methods=['POST'])
def update_chapter():
    chapter_id = request.form['chapter_id']
    try:
        chapter_instance = chapter.get_by_id(chapter_id)
        chapter_instance.chaptername = request.form['chapter_name']
        chapter_instance.numberofmembers = request.form['number_of_members']
        chapter_instance.chapterlead = request.form['chapter_lead']
        chapter_instance.chapteremail = request.form['chapter_email']
        chapter_instance.save()
        return redirect(url_for('main_page'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/events')
def events():
    events_query = event.select()
    event_data = [{
        'eventname': e.eventname,
        'venue': e.venue,
        'eventdate': e.eventdate.strftime('%Y-%m-%d'),
        'theme': e.theme,
        'attendance': e.numberofmembersattended
    } for e in events_query]
    return render_template("events.html", events=event_data)
@app.route('/donations')
def donations():
    donations_query = donation.select().join(member)
    donations_data = [{
        'donationId': d.donationId,
        'donor': d.donor.firstname + ' ' + d.donor.lastname,
        'item': d.item,
        'monetaryWorth': d.monetaryWorth
    } for d in donations_query]
    return render_template("donations.html", donations=donations_data)
@app.route('/add_member', methods=['POST'])
def add_member():
    try:
        new_member = member.create(
            firstname=request.form['first_name'],
            middlename=request.form.get('middle_name', ''),
            lastname=request.form['last_name'],
            phonenumber=request.form['phone_number'],
            score=request.form['score'],
            memberaddress=request.form['address'],
            numberofeventsattended=request.form['number_of_events_attended'],
            status=request.form['status']
        )
        new_member.save()
        return redirect(url_for('members'))
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 500
@app.route('/add_event', methods=['POST'])
def add_event():
    try:
        new_event = event.create(
            eventname=request.form['event_name'],
            venue=request.form['venue'],
            eventdate=datetime.strptime(request.form['event_date'], '%Y-%m-%d'),
            theme=request.form['theme'],
            numberofmembersattended=request.form['attendance']
        )
        return redirect(url_for('events'))
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 500
@app.route('/add_donation', methods=['POST'])
def add_donation():
    try:
        new_donation = donation.create(
            donor_id=request.form['donor_id'],
            item=request.form['item'],
            monetaryWorth=request.form['monetaryWorth']
        )
        return redirect(url_for('donations'))
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 500
@app.route('/update_event', methods=['POST'])
def update_event():
    try:
        event_instance = event.get_by_id(request.form['event_id'])
        event_instance.venue = request.form['venue']
        event_instance.eventdate = datetime.strptime(request.form['event_date'], '%Y-%m-%d')
        event_instance.theme = request.form['theme']
        event_instance.numberofmembersattended = request.form['attendance']
        event_instance.save()
        return redirect(url_for('events'))
    except event.DoesNotExist:
        return jsonify({'error': 'Event not found'}), 404
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 500
@app.route('/update_member', methods=['POST'])
def update_member():
    member_id = request.form['member_id']
    try:
        member_instance = member.get_by_id(member_id)
        member_instance.firstname = request.form['first_name']
        member_instance.middlename = request.form['middle_name']
        member_instance.lastname = request.form['last_name']
        member_instance.phonenumber = request.form['phone_number']
        member_instance.score = request.form['score']
        member_instance.memberaddress = request.form['address']
        member_instance.numberofeventsattended = request.form['number_of_events_attended']
        member_instance.status = request.form['status']
        member_instance.save()
        return redirect(url_for('members'))
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 500
def member_to_dict(member):
    return {
        "memberid": member.memberid,
        "firstname": member.firstname,
        "middlename": member.middlename,
        "lastname": member.lastname,
        "phonenumber": member.phonenumber,
        "score": member.score,
        "memberaddress": member.memberaddress,
        "numberofeventsattended": member.numberofeventsattended,
        "status": member.status
    }

# def fetch_attendees_for_event(event_name):
#     """Fetches attendees for a given event by its name using the Peewee ORM."""
#     try:
#         query = (event_attendance
#                  .select(member.firstname, member.lastname)
#                  .join(member)
#                  .switch(event_attendance)
#                  .join(event)
#                  .where(event.eventname == event_name))
#         attendees = [{'firstname': ea.member.firstname, 'lastname': ea.member.lastname} for ea in query]
#         return attendees
#     except Exception as e:
#         print(f"Error fetching attendees: {e}")
#         return []

# def fetch_attendees_for_event(event_name):
#     """Fetches attendees for a given event by its name using the Peewee ORM."""
#     try:
#         # Querying the event_attendance table and joining it with the member table
#         # to get the attendees for the given event name.
#         query = (event_attendance
#                  .select(member.firstname, member.lastname)
#                  .join(member)
#                  .where(event_attendance.event.eventname == event_name))
#         attendees = [{'firstname': attendee.member.firstname, 'lastname': attendee.member.lastname} for attendee in query]
#         return attendees
#     except Exception as e:
#         print(f"Error fetching attendees: {e}")
#         return []
def fetch_attendees_for_event(event_name):
    try:
        query = (event_attendance
                 .select(member.firstname, member.lastname)
                 .join(member)
                 .switch(event_attendance)
                 .join(event)
                 .where(event.eventname == event_name))
        attendees = [{'firstname': attendee.member.firstname, 'lastname': attendee.member.lastname} for attendee in query]
        print(f"Fetched attendees for {event_name}: {attendees}")  # Debug print
        return attendees
    except Exception as e:
        print(f"Error fetching attendees: {e}")
        return []



# Assuming you have a model or a way to fetch data from your database
# @app.route('/get_attendees')
# def get_attendees():
#     event_name = request.args.get('eventname')
#     attendees = fetch_attendees_for_event(event_name)  # You need to implement this function
#     return jsonify({
#         'attendees': [{'firstname': a.firstname, 'lastname': a.lastname} for a in attendees]
#     })
@app.route('/get_attendees')
def get_attendees():
    event_name = request.args.get('eventName')
    attendees = fetch_attendees_for_event(event_name)
    return jsonify({'attendees': attendees})




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
