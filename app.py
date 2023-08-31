import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.user_parameters_validator import UserParametersValidator
from lib.spaces import Spaces
from lib.spaces_repository import SpacesRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /
# Returns the homepage
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')


# GET AND POST /login
    # GET: Returns the login page
    # POST: 
        # - if login is valid, redirects to spaces page
        # - if login is invalid, redirects to login page, and displays an error
@app.route('/login', methods=['GET', 'POST'])
def get_post_login_page():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection) 
        email_address = request.form["email_address"]
        user_password = request.form["user_password"]
        login_status = repository.validate_login(email_address, user_password)
        if login_status:
            repository1 = SpacesRepository(connection)
            spaces = repository1.all()
            return render_template('spaces.html', spaces=spaces)
        else:
            return render_template('login.html', error="Please submit valid login.")

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/sign_up', methods=['POST'])
def add_user():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    validator = UserParametersValidator(
        request.form["first_name"],
        request.form["last_name"],
        request.form["email_address"],
        request.form["user_password"]
    )
    
    if not validator.is_valid():
        errors = validator.generate_errors()
        return render_template("sign_up.html", errors=errors)

    user = User(
        validator.get_valid_first_name(),
        validator.get_valid_last_name(),
        validator.get_valid_email_address(),
        validator.get_valid_user_password()
    )

    repo.add(user)
    return redirect(f"/")

@app.route('/new', methods=['GET'])
def get_login():
    return render_template('new.html')

@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces)

@app.route('/spaces/new', methods=['GET'])
def get_list_space_page():
    return render_template('spaces/new.html')

@app.route('/spaces/new', methods=['POST'])
def post_new_space():
    connection = get_flask_database_connection(app)
    repository = SpacesRepository(connection)
    title = request.form['title']
    description = request.form['description']
    email_address = request.form['email_address']
    price_per_night = request.form['price_per_night']
    user_id = request.form['user_id']
    new_space = Spaces(None, title, description, email_address, price_per_night, user_id)
    repository.create(new_space)
    return redirect(url_for('get_spaces'))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
