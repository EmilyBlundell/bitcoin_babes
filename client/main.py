import requests
import json
from simulator import *
from collections import namedtuple

'''def get_best_trader():


def get_worst_trader():


def display_all_traders():


def get_trader_stat(name):


def get_trader_group(trader_score):'''

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

    initial_crypto = 100

    print('Welcome to the trading simulator\nYou have 100 units of Bitcoin (BTC) to start trading with')

    first = input('Please enter your first name')
    last = input('Please enter your last name')

    #a = investment('BTC', 50)

    #first_play = switch_currency(initial_crypto)

    #print(type(first_play))

    #currency, amount = first_play

    stock = investment(switch_currency(initial_crypto))

    #a.gamble()

    #a.fluctuate()

    stock.gamble()

    a.fluctuate()

    a.free_crypto()

    print(f'After market fluctuations your final amount of {a.currency} is {a.amount}')

    print(f'You final score on this simulator is {a.score} meaning you have earnt {a.crypto} units of {a.currency}')

    new_trader = namedtuple('trader', ['first', 'last', 'score', 'crypto', 'currency'])

    newest_trader = new_trader(first, last, a.score, a.crypto, a.currency)



if __name__ == '__main__':
    run()