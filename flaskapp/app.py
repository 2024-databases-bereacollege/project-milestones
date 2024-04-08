"""
This is the main file for your Flask app, containing app set-up and all of the routes.
In a more complex application you would split your routes into other files as needed.
"""
from datetime import datetime

from flask import Flask, render_template, request


# from logic import *

app = Flask(__name__)

@app.route('/')
def admin_panel():
    # courses = Course.select()
    return render_template("index.html")

@app.route('/members')
def members():
    return render_template("members.html")

# @app.route('/register', methods=['POST'])
# def register():
#     """
#     """
#     course_id = request.form.get('course_id')
#     user_id = request.form.get('user_id')

#     StudentCourse.insert(course=course_id,
#                          student=user_id,registered_on=datetime.now()).execute()

#     return ''

# @app.route('/current/<int:id>', methods=['GET', 'POST'])
# def currentCourses(id):
#    ''' View courses for the given user
#    '''
#    mycourses = [Course.get(1),Course.get(2)]
#    return ""

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