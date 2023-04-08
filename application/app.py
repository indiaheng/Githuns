from flask import Flask, render_template

app = Flask(__name__)

categories = ["General Knowledge", "Music", "History", "Movies", "Science"]


@app.route("/")
def home():
    return "<h1>Home Page</h1>"


@app.route("/menu")
def menu():
    return render_template('menu.html', categories=categories)


@app.route("/start/<category>")
def start(category):
    return render_template('start.html', category=category)


# run the app in debug mode
# so app reloads when changes have been made
if __name__ == "__main__":
    app.run(debug=True)