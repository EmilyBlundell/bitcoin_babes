import mysql.connector
from api.config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    connect = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=db_name
    )
    return connect

def _map_values(traders):
    mapped = []
    for profile in traders:
        print(profile)
        mapped.append({
            'name': item[0],
            # add list of column names and item[] separated by commas - refer to SQL table structure
        })
    return mapped

# EXAMPLE 1 - Gets the trader/ traders with the highest score
def get_best_trader():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score
FROM investors_info
WHERE current_score IN (SELECT MAX(current_score)
						FROM investors_info);"""
        cur.execute(query)

        best_trader = _map_values(cur.fetchall())

    except Exception:
        raise  DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return best_trader

# Gets the trader/ traders with the lowest score
def get_worst_trader():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score
FROM investors_info
WHERE current_score IN (SELECT MIN(current_score)
						FROM investors_info);"""
        cur.execute(query)

        worst_trader = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return worst_trader


def display_all_traders():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score, crypto_balance
            FROM investors_info;"""
        cur.execute(query)

        all_traders = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return all_traders

### need to make an id variable ###
def get_trader_stat(id):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score, crypto_balance
        FROM investors_info
        WHERE investor_id = {}; """.format(id)
        cur.execute(query)

        trader_stat = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return trader_stat


def get_trader_group(trader_score):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score
        FROM investors_info
        WHERE current_score = {};""".format(trader_score)
        cur.execute(query)

        all_traders = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return all_traders

### earlier used trader_score as variable
def add_trader(id, first, last, score, crypto):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        update_booking = """INSERT INTO investors_info 
        VALUES({}, {}, {}, {},{})""".format(id, first, last, score, crypto)
        cur.execute(update_booking)

        nanodb.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("DB connection failed")
    finally:
        if nanodb:
            nanodb.close()

if __name__ == '__main__':
   print( display_all_traders())
