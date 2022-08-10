import mysql.connector
from config import HOST, USER, PASSWORD


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


def get_all():
    try:
        nanodb = _connect_to_db('nano')
        print('Connection opened')
        cur = nanodb.cursor()
        cur.execute("SELECT * FROM investors_info")
        result = cur.fetchall()

        for i in result:
            print(i)
    except Exception:
        raise DbConnectionError("Unable to connect to database")
    finally:
        if nanodb:
            nanodb.close()
            print("connection closed")


def _map_values(traders):
    mapped = []
    for profile in traders:
        print(profile)
        mapped.append({
            'investor_first_name',
            'investor_last_name',
            'current_score',
            'crypto_balance',
        })
    return mapped

# EXAMPLE 1 - Gets the trader/ traders with the highest score


def get_best_trader():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, investor_first_name, investor_last_name, current_score
        FROM investors_info
        WHERE current_score IN (SELECT MAX(current_score)
						FROM investors_info);"""
        cur.execute(query)

        best_trader = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
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
        query = """ SELECT investor_id, investor_first_name, investor_last_name, current_score
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
        query = """ SELECT investor_id, investor_first_name, investor_last_name, current_score, crypto_balance
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


# earlier used trader_score as variable
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


def get_trader_stat(investor_id):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ SELECT investor_id, current_score, crypto_balance
        FROM investors_info
        WHERE investor_id = {}; """.format(investor_id)
        cur.execute(query)

        trader_stat = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return trader_stat


def main():
    print(get_all())
    print(get_best_trader())
    print(get_worst_trader())
    print(display_all_traders())
    print(add_trader())
    print(get_trader_stat())


if __name__ == "__main__":
    main()
