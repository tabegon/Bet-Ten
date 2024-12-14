from flask import Flask, redirect

app = Flask(__name__,
            static_url_path='',
            static_folder='app/static')

@app.route("/")
def index():
    return redirect("/login.html", code=302)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"