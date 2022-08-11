import requests
import json
from simulator import *
from collections import namedtuple


def get_best_or_worst():
    result = requests.get(
        '127.0.0.1:5000/leader/best',
        headers={'content-type': 'application/json'})
    return result.json()


def get_worst_trader():
    result = requests.get(
        '127.0.0.1:5000/leader/worst',
        headers={'content-type': 'application/json'})
    return result.json()

# def get_best_or_worst(selection):
#     selection = selection.casefold()
#     if selection == 'best':
#         result_best = requests.get(
#             '127.0.0.1:5000/leader/best',
#             headers={'content-type': 'application/json'})
#         return result_best.json()
#     elif selection == 'worst':
#         result_worst = requests.get(
#             '127.0.0.1:5000/leader/worst',
#             headers={'content-type': 'application/json'})
#         return result_worst.json()
#     else:
#         return


def display_all_traders(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} ".format(
        'investor ID', 'current score', 'crypto balance'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} ".format(
            item['investor_id'], item['current_score'], item['crypto_balance']
        ))


def get_trader_stat(investor_id):
    result = requests.get(
        'http://127.0.0.1:5000/user/{}'.format(investor_id),
        headers={'content-type': 'application/json'}
    )
    return result.json()

# this may not be required as new user is part of trading simulation
# # def add_trader(first, last, score, crypto):
# #     trader = {
# #         "First_Name": first,
# #         "Last_Name": last,
# #         "Score": score,
# #         "Current_Balance": crypto,
# #     }

#     result = requests.put(
#         'http://127.0.0.1:5000/new',
#         headers={'content-type': 'application/json'},
#         data=json.dumps(trader)
#     )

#     return result.json()


def run():
    print('############################')
    print('Welcome to Test Trade, the add-on for validating trading prowess')
    print('############################')
    print()

    initial_crypto = 100

    print('Welcome to the trading simulator\nYou have 100 units of Bitcoin (BTC) to start trading with')
    print('############################')
    print()

    first = input('Please enter your first name')
    last = input('Please enter your last name')
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
        'trader', ['first', 'last', 'score', 'crypto', 'currency'])

    newest_trader = new_trader(
        first, last, stock.score, stock.crypto, stock.currency)

    print(
        f'Welcome new trader\nYour registration details are as follows: {newest_trader}')
    print('############################')
    print()


def views():
    print('############################')
    print()
    print('To get the best trader, please type: best')
    print('To get the worst trader, please type: worst')
    print('To get a trader\'s stats, please type the trader\'s id number')
    print('To view the leaderboard, please type: leaderboard')
    print('To view all traders, please type: alltraders')
    selection = input('Please type here what you would like to view: ')
    print(get_best_or_worst(selection))

    # if selection == 'best':
    #     return get_best_trader(selection)
    # elif selection == 'worst':
    #     return get_worst_trader
    # # elif selection == int:
    # #     return get_trader_stat(investor_id)
    # else:
    #     return 'Please select an option from above'


if __name__ == '__main__':
    run()
    views()

# if run():
#     return views()
