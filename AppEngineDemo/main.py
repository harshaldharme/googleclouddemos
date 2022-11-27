from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return '<body style="background-color: lightgreen"><br/><h1> Welcome to Edureka Learning Portal </h1><h4> Take a look at Google Cloud Cheatsheet </h4><p></p><p></p><img src=\'https://www.googlecloudcommunity.com/gc/image/serverpage/image-id/41615iF0164B367E605DE8?v=v2\'></body>'
