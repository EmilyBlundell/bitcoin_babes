
# Test Trade Simulation (Bitcoin_Babes_Project)

## Description
The objective of our project is to allow traders to be given a score based on their ability to trade and have good investor practice. To first obtain data on the traders a trading simulation will be completed on the app. The trading simulation will provide an initial trading score which will dictate how much preliminary digital currency they will be given to trade with on the platform. Users are then able to view the best or worst trader, all traders or a specific trader. We aim to be transparent and make it easier for beginners to start trading with cryptocurrencies. \
We run this through the command line. 

## Requirements

1. Python 3
2. The pip installer package
3. MySQL

## Installation

1. Clone files from remote repository on Github to your local repository
2. Use pip to install: 
* requests 
* collections
* json
* mysql.connector
* Flask
* time
* randon
* itertools
* math
* unittest

3. Go to MySQL and open the file called create_nano_db_script.sql and run the script
4. Go to the config.py file and insert your password for MySQL
5. In the command line/terminal, navigate to the folder containing the API files.
6. Run the following command:
```shell
> export FLASK_ENV=development
> flask run
```
7. In the command line, run the main.py file
8. Open your browser and open the urls with the different endpoints in the app.py file
## Authors

Iman Kasmani, Emily Blundell, Rebecca Clarke, Promise Edah Frank and Amanda Gitau

## License

An open source project created by the authors above. 

## Project Status
Once the project was submitted on 14/08/2022, development has stopped. 