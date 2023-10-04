from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# In-memory storage for the prototype. In a real application, use a database.
inventory = []

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    global inventory
    df = pd.read_excel(file)
    inventory = df.to_dict(orient='records')
    return jsonify({"message": "Uploaded successfully!"}), 200

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == "__main__":
    app.run(debug=True)
