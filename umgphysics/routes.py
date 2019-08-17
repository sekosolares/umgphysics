from flask import render_template
from umgphysics import app


@app.route("/")
@app.route("/home")
def index():
    title = "UMG - Physics Course | Home"
    return render_template('index.html', title=title)


@app.route("/lesson1")
def lesson1():
    title = "UMG - Physics Course | Lesson 1"
    return render_template('lesson1.html')
