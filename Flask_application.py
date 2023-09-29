from flask import Flask
app = Flask(__name__)

@app.route('/')
def my_flask_application():
    return 'welcome to updated yaml of circleci..testing for image updation check.. check dangling'

