#use command below to run the API
#flask --app app run


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello"

