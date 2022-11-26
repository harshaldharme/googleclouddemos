from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<body style="background-color: lightblue"><br/><h1> Welcome to Edureka Learning Portal </h1><h4> Course Contents </h4><p></p><p>Introduction to <strong>Google App Engine</strong></p><p></p><p>Your New Instructor: <strong>Jennica</strong></p><img src=\'https://freepngimg.com/save/35555-teacher-clipart/512x512\'></body>'
