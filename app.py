from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

CSV_PATH = "Inventory.csv"

@app.route('/inventory', methods=['GET'])
def get_inventory():
    df = pd.read_csv(CSV_PATH)
    inventory = df.to_dict(orient='records')
    return jsonify(inventory)

@app.route('/request-items', methods=['POST'])
def request_items():
    data = request.json
    item_name = data.get('item_name')
    amount = data.get('amount')

    df = pd.read_csv(CSV_PATH)
    idx = df[df['Item name'] == item_name].index[0]
    if df.at[idx, 'quantity of item'] < amount:
        return jsonify({"message": "Not enough items in inventory"}), 400

    df.at[idx, 'quantity of item'] -= amount
    df.to_csv(CSV_PATH, index=False)
    return jsonify({"message": "Request successful"}), 200

if __name__ == "__main__":
    app.run(debug=True)
