import sqlite3

# Connect to / Create  DB
conn = sqlite3.connect('money.db')

# Cursor
c = conn.cursor()

# Create a table
s_sql = '''
    CREATE TABLE IF NOT EXISTS checking (
    asof_date text,
    description text,
    payment_amt real,
    deposit_amt real,
    balance real
    )
'''

# Drop table if needed 
# s_sql = '''DROP TABLE IF EXISTS checking'''

c.execute(s_sql)


# Commit sql
conn.commit()

# Close connection
conn.close()