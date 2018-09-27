import json
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    response = {
        'answer': data.get('question', '') + '?'
    }
    return json.dumps(response)
