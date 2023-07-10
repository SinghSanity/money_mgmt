import sqlite3

def select_helper(attributes=[], table=None, where_clause = ''):
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
        print("Caught this error in select_helper: " + str(e))

    # Try to execute the query and return data
    try:
        conn = sqlite3.connect('money.db')
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


