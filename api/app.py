from flask import Flask, request, jsonify
from scripts.handle_call_event import process_call_event

app = Flask(__name__)

@app.route('/call', methods=['POST'])
def handle_call():
    data = request.get_json()
    process_call_event(data)
    return jsonify({"status": "OK"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)