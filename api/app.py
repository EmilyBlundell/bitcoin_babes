from flask import Flask, jsonify, request
import api.db_utils as dbutils


app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Welcome to Test Trade, the add-on for validating trading prowess</h1>'


@app.route('/leader/<selection>')
def get_best_or_worst(selection):
    selection = selection.casefold()
    if selection == 'best':
        trader = dbutils.get_best_trader()
        return jsonify(trader)
    elif selection == 'worst':
        trader = dbutils.get_worst_trader()
        return jsonify(trader)
    else:
        return 'Wrong input'


@app.route('/new', methods=['PUT'])
def new_trader():
    trader = request.get_json()
    dbutils.add_trader(

        investor_id=trader["investor_id"],
        first_name=trader["investor_first_name"],
        last_name=trader["investor_last_name"],
        score=trader["current_score"],
        crypto=trader["crypto_balance"],
        currency=trader['currency']
    )
    return trader


@app.route('/user/<int:investor_id>')
def get_user_info(investor_id):
    trader = dbutils.get_trader_stat(investor_id)
    return jsonify(trader)


@app.route('/allinvestors')
def get_all_investors():
    trader = dbutils.display_all_traders()
    return jsonify(trader)


@app.route('/mostrecent')
def get_recent_user():
    trader = dbutils.get_recent_id()
    return jsonify(trader)

@app.route('/recentid')
def get_new_trader_id():
    trader = dbutils.get_recent_id()
    return jsonify(trader)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
