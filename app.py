import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_home():
    return render_template('index.html')

# GET /new
# Returns the login page
# Try it:
#   ; open http://localhost:5000/index
@app.route('/new', methods=['GET'])
def get_login():
    return render_template('new.html')

# GET /spaces
# Returns the spaces page
# Try it:
#   ; open http://localhost:5000/spaces
@app.route('/spaces', methods=['GET'])
def get_spaces():
    return render_template('spaces.html')

# GET /requests
# Returns the requests page
# Try it:
#   ; open http://localhost:5000/spaces
@app.route('/requests', methods=['GET'])
def get_requests():
    return render_template('requests.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
