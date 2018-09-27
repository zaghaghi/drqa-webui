import json
from flask import Flask, render_template, request
app = Flask(__name__)

from services import DrQA, process

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    answers = process(question=data['question'])
    return json.dumps(answers)
