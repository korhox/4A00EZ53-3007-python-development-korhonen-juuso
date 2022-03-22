
from flask import Flask
from flask import render_template
from flask import make_response
from flask import request

app = Flask(__name__)


@app.route("/")
def main():
    if "money" in request.cookies:
        money = request.cookies.get("money")
        if money <= 0:
            request.cookies.delete_cookie("money")
    else:
        response = make_response()
        response.set_cookie("money", 20)

    return render_template('index.html', money=money)


if __name__ == "__main__":
    app.run(debug=True)
