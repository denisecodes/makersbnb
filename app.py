import os
from flask import Flask, request, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /
# Returns the homepage
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /spaces
# Returns the spaces page
@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')


# GET AND POST /login
    # GET: Returns the login page
    # POST: 
        # - if login is valid, redirects to spaces page
        # - if login is invalid, redirects to login page, and displays an error
@app.route('/login', methods=['GET', 'POST'])
def get_login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection) 
        email_address = request.form["email_address"]
        user_password = request.form["user_password"]
        login_status = repository.validate_login(email_address, user_password)
        if login_status:
            return redirect('/spaces')
        else:
            return render_template("login.html", error="Please submit valid login.")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
