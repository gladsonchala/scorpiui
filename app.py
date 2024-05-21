import os
from flask import Flask, render_template, request
from scorpiui.components.button import Button

app = Flask(__name__)

# Store event handlers
event_handlers = {}

# @app.route('/')
# def home():
#     return render_template('base.html', content="")

@app.route('/_event', methods=['POST'])
def handle_event():
    event_data = request.get_json()
    event_id = event_data.get('event_id')
    if event_id in event_handlers:
        event_handlers[event_id]()
    return '', 204

def register_event(event_id, handler):
    event_handlers[event_id] = handler

def run_app():
    app.run(debug=True)
