'''Contains utility functions for the database'''
import os
import sqlite3
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
GLOBAL_DB = os.getenv('GLOBAL_DB')

def select_helper(attributes=None, table=None, where_clause='', order_by_clause=None, as_df=False):
    '''
    Helper function to query select statements from the table

    Parameters:
    attributes:     Type: list      : Default: None     :   A list of attributes you want to select from the table. 
    table:          Type: string    : Default: None     :   The table name you want to query.
    where_clause:   Type: string    : Default: ''       :   Clause and conditions on how you want to query the data.
    order_by_clause Type: string    : Default: None     :   Clause used to order the data in the query.
    as_df           Type: bool      : Default: False    :   Changes the return type to a df instead of list of tuples.
    '''
    items = ''
    table_name = table
    condition = ''
    order_by = ''
    s_sql = ''

    try:
        if not attributes:
            attributes = ['*']
        items = ', '.join(attributes)

        if not table_name:
            raise Exception("No table name provided")

        if where_clause:
            condition = 'WHERE ' + where_clause

        if order_by_clause:
            order_by = 'ORDER BY ' + order_by_clause

        s_sql = '''
            SELECT {0} FROM {1} {2} {3}
        '''.format(items, table_name, condition, order_by)

    except Exception as e:
        print("Caught this error in select_helper: " + repr(e))
        return None

    # Try to execute the query and return data
    try:
        conn = sqlite3.connect(GLOBAL_DB)
        # Cursor
        c = conn.cursor()

        print("Executing query: " + s_sql)

        c.execute(s_sql)
        rows = c.fetchall()

        value = rows
        if as_df:
            value = pd.DataFrame(rows, columns=[desc[0] for desc in c.description])

        # Commit sql
        conn.commit()
        # Close connection
        conn.close()

        return value
    except Exception as e:
        print("Caught this error while querying the table: " + str(e))
        return None
