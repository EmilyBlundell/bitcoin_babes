from simulator import *
from collections import namedtuple
import requests
import json


# function to get the best trader
def get_best_trader():
    result = requests.get(
        'http://127.0.0.1:5000/leader/best',
        headers={'content-type': 'application/json'})
    return result.json()


# function to get the worst trader
def get_worst_trader():
    result = requests.get(
        'http://127.0.0.1:5000/leader/worst',
        headers={'content-type': 'application/json'})
    return result.json()


# function to format the display of results
def display_results(records):
    # Print the names of the columns.
    print("{:<20} {:<20} {:<20} {:<20} {:<20} ".format(
        'investor ID', 'investor_first_name', 'investor_last_name', 'current score', 'currency'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<20} {:<20} {:<20} {:<20} {:<20} ".format(
            item['investor_id'], item['investor_first_name'], item['investor_last_name'], item['current_score'],
            item['currency']
        ))


# function to get all traders
def get_all_traders():
    result = requests.get(
        'http://127.0.0.1:5000/allinvestors',
        headers={'content-type': 'application/json'})
    return result.json()


# function to get individual trader stats with their investor id number
def get_trader_stat(investor_id):
    result = requests.get(
        'http://127.0.0.1:5000/user/{}'.format(investor_id),
        headers={'content-type': 'application/json'}
    )
    trader_info = json.loads(result.text)
    return trader_info


def get_new_trader_id():
    result = requests.get(
        'http://127.0.0.1:5000/recentid',
        headers={'content-type': 'application/json'})
    return result.json()


# function to add a new trader
def add_trader(investor_id, first_name, last_name, score, crypto, currency):
    trader = {
        "investor_id": investor_id,
        "investor_first_name": first_name,
        "investor_last_name": last_name,
        "crypto_score": score,
        "current_balance": crypto,
        "currency": currency

    }

    result = requests.put(
        'http://127.0.0.1:5000/new',
        headers={'content-type': 'application/json'},
        data=json.dumps(trader)
    )

    return result.json()


# function to run the trading simulation
def run():
    print('############################')
    print('Welcome to Test Trade, the add-on for validating trading prowess')
    print('############################')
    print()

    initial_crypto = 100

    print('Welcome to the trading simulator\nYou have 100 units of Bitcoin (BTC) to start trading with')
    print('############################')
    print()

    first_name = input('Please enter your first name ')
    last_name = input('Please enter your last name ')
    print('############################')
    print()

    currency, amount = switch_currency(initial_crypto, 'BTC')
    print('############################')
    print()

    stock = investment(currency, amount)

    stock.fluctuate()
    print('############################')
    print()

    stock.gamble()
    print('############################')
    print()

    stock.fluctuate()
    print('############################')
    print()

    stock.free_crypto()
    print('############################')
    print()

    print(
        f'After market fluctuations and gambling your final amount of {stock.currency} is {stock.amount}')
    print('############################')
    print()

    print(
        f'You final score on this simulator is {stock.score} meaning you have earnt {stock.crypto} units of {stock.currency}')
    print('############################')
    print()

    new_trader = namedtuple(
        'trader', ['id', 'first', 'last', 'score', 'crypto', 'currency'])

    investor_id = get_new_trader_id() + 1

    newest_trader = new_trader(
        investor_id, first_name, last_name, stock.score, stock.crypto, stock.currency)

    print(
        f'Welcome new trader\nYour registration details are as follows: {newest_trader}')
    print('############################')
    print()

    add_trader(investor_id, first_name, last_name,
               stock.score, stock.crypto, stock.currency)


# function to view if users would like to obtain the best or worst trader, all traders or a specific trader
def views():
    print('############################')
    print()
    print('To get the best trader, please type: best')
    print('To get the worst trader, please type: worst')
    print('To get a trader\'s stats, please type: trader stats')
    print('To view all traders, please type: all')
    selection = input('Please type here what you would like to view: ')
    selection = selection.casefold()
    if selection == 'best':
        best_trader = get_best_trader()
        display_results(best_trader)
    elif selection == 'worst':
        worst_trader = get_worst_trader()
        display_results(worst_trader)
    elif selection == 'trader stats':
        id_number = input('Please type the trader\'s id number: ')
        trader_stat = get_trader_stat(id_number)
        print("{:<20} {:<20} {:<20} {:<20} {:<20} ".format(
            'investor ID', 'investor_first_name', 'investor_last_name', 'current score', 'currency'))
        print('-' * 105)
        values = list(trader_stat.values())
        print("{:<20} {:<20} {:<20} {:<20} {:<20} ".format(
            values[2], values[3], values[5], values[0], values[1]
        ))
    elif selection == 'all':
        all_traders = get_all_traders()
        display_results(all_traders)
    else:
        return


if __name__ == '__main__':
    run()
    views()
