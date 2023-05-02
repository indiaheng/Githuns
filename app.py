from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__, static_folder='home-page-with-flask/static')


@app.route('/', methods=['GET', 'POST'])



if __name__ == '__main__':
    app.run(debug=True)

