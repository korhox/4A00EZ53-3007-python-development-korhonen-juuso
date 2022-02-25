from flask import Flask
from datetime import datetime

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root


@app.route("/hello")
def hello_world():
    return "<p>Hello World</p>"


@app.route("/juuso")
def juuso():
    return "<p>Juuso</p>"


@app.route("/date")
def date():
    date = datetime.now()
    return f"<p>{date}</p>"


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)
