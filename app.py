import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
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

@app.route('/sign_up', methods=['GET'])
def get_sign_up():
    return render_template('sign_up.html')

@app.route('/sign_up', methods=['POST'])
def add_user():
    connection = get_flask_database_connection(app)
    user = User(
        request.form["first_name"],
        request.form["last_name"],
        request.form["email_address"],
        request.form["user_password"]
    )
    repo = UserRepository(connection)
    repo.add(user)
    return redirect(f"/index")

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 8000)))
