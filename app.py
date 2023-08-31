import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.spaces import Spaces
from lib.spaces_repository import SpacesRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# GET /new
# Returns the login page
# Try it:
#   ; open http://localhost:5000/index
@app.route('/new', methods=['GET'])
def get_login():
    return render_template('new.html')

# GET /requests
# Returns the requests page
# Try it:
#   ; open http://localhost:5000/spaces
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
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
