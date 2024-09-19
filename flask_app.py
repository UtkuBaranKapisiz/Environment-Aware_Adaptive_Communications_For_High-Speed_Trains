from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for the latest values of both data sets
latest_data = {"node_1": None, "node_2": None}
latest_data2 = {"node_3": None, "node_4": None}

@app.route('/post_data', methods=['POST'])
def receive_data():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    node_1 = data.get('node_1')
    node_2 = data.get('node_2')

    if node_1 is None or node_2 is None:
        return jsonify({"error": "Missing 'node_1' or 'node_2' data"}), 400

    # Update the latest data
    latest_data["node_1"] = node_1
    latest_data["node_2"] = node_2

    return jsonify({"message": "Data received successfully"}), 200

@app.route('/get_latest', methods=['GET'])
def send_latest_data():
    if latest_data["node_1"] is None or latest_data["node_2"] is None:
        return jsonify({"error": "No data available"}), 404

    return jsonify(latest_data), 200

@app.route('/post_data2', methods=['POST'])
def receive_data2():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    node_3 = data.get('node_3')
    node_4 = data.get('node_4')

    if node_3 is None or node_4 is None:
        return jsonify({"error": "Missing 'node_3' or 'node_4' data"}), 400

    # Update the latest data for the second set
    latest_data2["node_3"] = node_3
    latest_data2["node_4"] = node_4

    return jsonify({"message": "Data received successfully"}), 200

@app.route('/get_latest2', methods=['GET'])
def send_latest_data2():
    if latest_data2["node_3"] is None or latest_data2["node_4"] is None:
        return jsonify({"error": "No data available"}), 404

    return jsonify(latest_data2), 200

@app.route('/')
def hello_world():
    return 'Choof Choof!'

# Omitted app.run() for PythonAnywhere hosting
