from flask import Flask, request, render_template
from scorpiui.event_handler import handle_event

app = Flask(__name__)

@app.route('/_event', methods=['POST'])
def event_route():
    event_data = request.get_json()
    event_id = event_data.get('event_id')
    handle_event(event_id, event_data)
    return '', 204

def run_app():
    app.run(debug=True)
