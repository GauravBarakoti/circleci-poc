from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
    return 'green works test case 28'

