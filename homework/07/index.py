
from flask import Flask
from flask import render_template
from flask import request
from repository import *
from string_helper import *
from validation import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        if is_name(fname) == True and is_name(lname) == True:
            save_to_database(fname, lname)
    return render_template('index.html', db=csv_to_list(read_database()))


if __name__ == "__main__":
    app.run(debug=True)
