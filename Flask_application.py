from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
    return 'testing for zero downtime 50 attempt'

