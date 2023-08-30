import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def get_login():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email_address = request.form["email_address"]
    user_password = request.form["user_password"]
    login_status = repository.validate_login(email_address, user_password)
    if login_status == True:
        return redirect('/spaces')
    
    

# @app.route('/spaces', methods=['GET','POST'])
# def  get_spaces_if_login_successful():
#     connection = get_flask_database_connection(app)
#     repository = UserRepository(connection)
#     email_address = request.form["Email Address"]
#     user_password = request.form["Password"]
#     login_status = repository.validate_login(email_address, user_password)
#     if login_status == True:
#         return redirect('/spaces')



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
