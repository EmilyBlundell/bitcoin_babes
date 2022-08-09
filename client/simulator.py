
import requests
import time
import random
import itertools
import math

class investment():

    def __init__(self, currency, amount):
          self.currency = currency
          self.amount = amount
          self.score = 0
          self.crypto = 0

    def fluctuate(self):

        fluctuation = round(random.uniform(0, 2), 2)
        self.amount = round((int(self.amount) * fluctuation), 2)
        print(f'There has been a {fluctuation} fluctuation in the market\nYour new balance of {self.currency} is {self.amount}')


    def gamble(self):

        take_chance = input('''Would you like to enter a random gamble?
        \nThis function will scramble the numbers of your current balance, potentially to your advantage: y/n''')

        if take_chance == 'y':

            iter_amount = str(self.amount)

            gambles = list(itertools.permutations(iter_amount))

            possibilities = num_permutations(len(iter_amount))

            choice = random.randint(0, possibilities-1)

            self.amount = gambles[choice]

            self.amount = "".join(self.amount)

            print(f'Your new total of {self.currency} is {self.amount}')

    def free_crypto(self):

        self.score = round(math.log(self.amount, 2), 2)
        self.crypto = round((self.score **2), 2)


def num_permutations(n):
        if n == 1:
            return n
        else:
            return n * num_permutations(n - 1)

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

        print('API requests ready again')

    return inner_wrapper

@timer
def switch_currency(crypto):

    switch_currency = input('Would you like to start trading in another digital currency instead?\nEnter y or n')

    crypto = crypto

    new_currency = 'BTC'

    available_currencies = ['ETH', 'USDT', 'BNB', 'XRP']

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

    return new_currency, crypto



