import requests
import json


def get_best_trader():


def get_worst_trader():


def display_all_traders():


def get_trader_stat(name):


def get_trader_group(trader_score):

def add_trader(first, last, score, crypto):
    trader = {
        "First_Name": first,
        "Last_Name": last,
        "Score": score,
        "Current_Balance": crypto,
    }

    result = requests.put(
        'http://127.0.0.1:5000/new',
        headers={'content-type': 'application/json'},
        data=json.dumps(trader)
    )

    return result.json()

def run():
    print('############################')
    print('Welcome to Test Trade, the add-on for validating trading prowess')
    print('############################')
    print()

    ### Logic for trading simulator goes here ###

if __name__ == '__main__':
    run()