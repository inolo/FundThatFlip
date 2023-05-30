import sqlite3
import requests
from sql_queries import create_table, neo_insert, create_error_log, log_error
from api_calls import get_call

if __name__ == '__main__':

    """Create/Connect to DB and create the main table"""
    try:
        conn = sqlite3.connect('./nasa.db')
        c = conn.cursor()
        create_table(c)
        create_error_log(c)
    except Exception as e:
        print("UNABLE TO CONNECT TO DATABASE")
        print(e)

    """Try to get the NEO data. """
    try:
        start_date = '1982-12-10'
        response = get_call(start_date)
    except Exception as e:
        log_error(c, e, conn)

    """Insert the data into the main table"""
    try:
        neo_insert(response, c, conn)
    except Exception as e:
        log_error(c, e, conn)
