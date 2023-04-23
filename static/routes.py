from flask import render_template
from Githuns.application import app


@app.route('/home')
def home():
    return render_template('home,html')


@app.route('/welcome/home')
def index():
    return render_template('welocme.html,name=name,group='everyone')

@app.route('/')
def index():
    return render_template('home,html')