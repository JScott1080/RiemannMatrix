from flask import Flask, render_template, request, jsonify
import asyncio
import websockets
import json

app = Flask(__name__)

# To store the universal filter
universal_filter = []

# WebSocket connection to the AI server
async def send_websocket_message(message):
    async with websockets.connect("ws://localhost:8000") as websocket:
        await websocket.send(json.dumps(message))
        response = await websocket.recv()
        return response

# Index route to render the dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Route to push passive prompt
@app.route('/push_prompt', methods=['POST'])
def push_prompt():
    prompt = request.form['prompt']
    asyncio.run(send_websocket_message({"type": "prompt", "prompt": prompt}))
    return jsonify({"status": "success"})

# Route to abort response
@app.route('/abort_response', methods=['POST'])
def abort_response():
    asyncio.run(send_websocket_message({"type": "command", "command": "abort"}))
    return jsonify({"status": "success"})

# Route to update universal filter
@app.route('/update_filter', methods=['POST'])
def update_filter():
    global universal_filter
    aborted_prompt = request.form['aborted_prompt']
    universal_filter.append(aborted_prompt)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
