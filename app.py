from flask import render_template, request
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/reg", methods=["GET"])
def reg():
    if request.method == "GET":
        x = request.args.get('p')
    return render_template('index.html', x=x)
