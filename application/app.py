from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/menu")
def menu():
    return "<h1>Trivia Categories</h1>"

# run the app in debug mode
# so app reloads when changes have been made
if __name__ == "__main__":
    app.run(debug=True)