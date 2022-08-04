from flask import Flask, jsonify, request
import api.db_utils as dbutils


app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Welcome to Test Trade, the add-on for validating trading prowess</h1>'

@app.route('/best')
def get_availability(date):
    trader = dbutils.get_best_trader()
    return jsonify(trader)

@app.route('/new', methods=['PUT'])
def new_trader():
    trader = request.get_json()
    dbutils.add_trader(
        first = trader['First_Name'],
        last = trader['Last_Name'],
        score = trader['Score'],
        crypto = trader['Current_Balance']
    )
    return trader


if __name__ == '__main__':
    app.run(debug=True, port=5001)