from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('problems.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        return "❌ Error: problems.json not found. Check file location!"

    topics = list(data.keys())
    return render_template('index.html', topics=topics)

@app.route('/topic/<topic_name>')
def show_topic(topic_name):
    try:
        with open('problems.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        return "❌ Error: problems.json not found. Check file location!"

    problems = data.get(topic_name.lower(), [])
    return render_template('topic.html', topic=topic_name.capitalize(), problems=problems)

app.run(host='0.0.0.0', port=81)
