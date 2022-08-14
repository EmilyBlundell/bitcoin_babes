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
        self.amount = round((self.amount * fluctuation), 2)
        print(f'There has been a {fluctuation} fluctuation in the market\nYour new balance of {self.currency} is {self.amount}')


    def gamble(self):

        if len(str(self.amount)) <= 3:

            take_chance = input('''Would you like to enter a random gamble?
            \nThis function will scramble the numbers of your current balance, potentially to your advantage: y/n''')

            if take_chance == 'y':

                iter_amount = str(self.amount)

                gambles = list(itertools.permutations(iter_amount))

                possibilities = num_permutations(len(iter_amount))

                choice = random.randint(0, possibilities-1)

                self.amount = gambles[choice]

                self.amount = int("".join(self.amount))

                print(f'Your new total of {self.currency} is {self.amount}')

        else:

            take_chance = input('''Would you like to enter a random gamble?
                        \nThis function will potentially add a 0 to the end of your balance (1 in 500 chance): y/n''')

            if take_chance == 'y':

                chance = random.randint(0,499)

                if chance == 0:

                    self.amount = self.amount*10
                    print(f'Congratulations you won against the odds, your new balance is {self.amount} units of {self.currency}')

                else:

                    self.amount = self.amount
                    print(f'Unlucky, your balance of {self.amount} units of {self.currency} remains unchanged')


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
        result = func(*args, **kwargs)
        print('Please wait 60 seconds for API request max to reload')
        t = 0
        while t < 60:

            if t == 30:
                print('30 seconds remaining, thank-you for your patience')
            time.sleep(1)
            t += 1

        print('API requests ready again')

        return result

    return inner_wrapper

@timer
def switch_currency(crypto, dig_currency):

    switch_currency = input(f'Would you like to exchange your current balance of {crypto} in {dig_currency} to another digital currency instead?\nEnter y or n')

    available_currencies = ['BTC', 'ETH', 'BNB', 'XRP']

    if switch_currency == 'y':

        for currency in available_currencies:

            url = f'https://rest.coinapi.io/v1/exchangerate/{dig_currency}/{currency}'
            headers = {'X-CoinAPI-Key': '45396587-1645-446A-B180-B88D3EF5654E'}
            response = requests.get(url, headers=headers)
            data = response.json()
            name = data["asset_id_quote"]
            rate = data["rate"]


            print(f'Exchange rate from {dig_currency} to {name} = {rate}')

        new_currency = input('Enter the 3 letter code of the currency you would like to exchange to')
        url = f'https://rest.coinapi.io/v1/exchangerate/{dig_currency}/{new_currency}'
        headers = {'X-CoinAPI-Key': '45396587-1645-446A-B180-B88D3EF5654E'}
        response = requests.get(url, headers=headers)
        data = response.json()
        exchange_rate = float(data["rate"])
        crypto = crypto * exchange_rate

        print(f'You now have {crypto} units of {new_currency}')

    return new_currency, crypto
