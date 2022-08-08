'''

This code will be used in the main.py file for the client to interact with


'''

import requests
import time
import random

class investment():

    def __init__(self, currency, amount):
          self.currency = currency
          self.amount = amount

    def fluctuate(self):

        fluctuation = round(random.uniform(0, 2), 2)
        self.amount = self.amount * fluctuation
        print(f'There has been a {fluctuation} fluctuation in the market\nYour new balance of {self.currency} is {self.amount}')



def timer(func):

    def inner_wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('Please wait 60 seconds for API request max to reload')
        t = 0
        while t < 60:

            if t == 30:
                print('30 seconds remaining, thank-you for your patience')
            time.sleep(1)
            t += 1

        print('API reqeuests ready again')

    return inner_wrapper

'''def market_fluctuation(func):

    def inner_wrapper(*args, **kwargs):

        func(*args, **kwargs)

        fluctuation = random.randint(0,1)

        if fluctuation:

            crypto= crypto *0.75

        else:



    return inner_wrapper
'''


crypto = 100

available_currencies = ['ETH', 'USDT','BNB', 'XRP']

print('Welcome to the trading simulator\nYou have 100 units of Bitcoin (BTC) to start trading with')

@timer
def switch_currency(crypto):

    switch_currency = input('Would you like to start trading in another digital currency instead?\nEnter y or n')

    if switch_currency == 'y':

        for currency in available_currencies:

            url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency={currency}&apikey=W1YOUK71XA85OSKU'
            r = requests.get(url)
            data = r.json()
            name = data["Realtime Currency Exchange Rate"]["4. To_Currency Name"]
            abbreviation = data["Realtime Currency Exchange Rate"]["3. To_Currency Code"]
            rate = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]


            print(f'Exchange rate from Bitcoin to {name} ({abbreviation}) = {rate}')

        new_currency = input('Enter the 3 letter code of the currency you would like to exchange to')
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency={new_currency}&apikey=W1YOUK71XA85OSKU'
        r = requests.get(url)
        data = r.json()
        exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        crypto = crypto * exchange_rate
        print(f'You now have {crypto} units of {new_currency}')


def invest():









'''
from collections import namedtuple

score = simulate()

new_trader = namedtuple('trader', ['first', 'last', 'score', 'crypto'])'''




