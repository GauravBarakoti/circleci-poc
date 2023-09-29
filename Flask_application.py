from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
    return 'Welcome to first Flask application, Hi all from runner circleci.........testing this.....removing specific container........changing configuration deploy new ______________'

