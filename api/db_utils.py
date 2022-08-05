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

# EXAMPLE 1


def get_best_trader():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ INSERT SQL QUERY HERE"""
        cur.execute(query)

        best_trader = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return best_trader


def get_worst_trader():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ INSERT SQL QUERY HERE"""
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
        query = """ INSERT SQL QUERY HERE"""
        cur.execute(query)

        all_traders = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return all_traders


def get_trader_stat():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ INSERT SQL QUERY HERE"""
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
        query = """ INSERT SQL QUERY HERE"""
        cur.execute(query)

        all_traders = _map_values(cur.fetchall())

    except Exception:
        raise DbConnectionError("Failed to connect to the database")
    finally:
        if nanodb:
            nanodb.close()
            print('Connection Closed')

    return all_traders


def add_trader(first, last, score, crypto):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        update_booking = """INSERT SQL QUERY""".format(
            first=first, last=last, score=score, crypto=crypto)
        cur.execute(update_booking)

        nanodb.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("DB connection failed")
    finally:
        if nanodb:
            nanodb.close()


def get_leader_board():
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        query = """ 
        # CREATE INDEX - will have large amounts of data 
        # SELECT ....
        # FROM ....
        # LEFT JOIN ....
        # ON x = y
        # GROUP BY ...
        # ORDER BY points DESC LIMIT 3;
        # """.format
        # cur.execute(query)

        top_3_users = _map_values(cur.fetchall())
    except Exception:
        raise DbConnectionError("Failed to read from the database")
    finally:
        if nanodb:
            nanodb.close()
            print('DB connection closed')

    return top_3_users


def add_points(username, additional_points):
    try:
        nanodb = _connect_to_db('nano')
        cur = nanodb.cursor()
        update_users = """
        # need to add points to current point in table but do not want to make new column
        UPDATE user SET current_points = current_points + {additional_pints} WHERE user_id/name = {username}  ???? - need to check this 
        """.format(username=username, additional_points=additional_points)
        cur.execute(update_users)

        nanodb.commit()
        cur.close()
    except Exception:
        raise DbConnectionError("DB connection failed")
    finally:
        if nanodb:
            nanodb.close()


if __name__ == '__main__':
    print(display_all_traders())
