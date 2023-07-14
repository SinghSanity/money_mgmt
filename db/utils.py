'''Contains utility functions for the database'''
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
GLOBAL_DB = os.getenv('GLOBAL_DB')

def select_helper(attributes=None, table=None, where_clause = ''):
    '''Helper function to select from the table'''
    items = ''
    table_name = table
    condition = ''
    s_sql = ''

    try:
        if not attributes:
            attributes = ['*']
        items = ', '.join(attributes)

        if not table_name:
            raise Exception("No table name provided")

        if where_clause:
            condition = 'WHERE ' + where_clause

        s_sql = '''
            SELECT {0} FROM {1} {2}
        '''.format(items, table_name, condition)

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

        # Commit sql
        conn.commit()
        # Close connection
        conn.close()

        return rows
    except Exception as e:
        print("Caught this error while querying the table: " + str(e))
        return None
