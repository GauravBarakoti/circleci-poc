from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
    return '55555555555555555555555555555555555555555555555555555555'

