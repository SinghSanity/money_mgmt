import sqlite3

# Connect to / Create  DB
conn = sqlite3.connect('money.db')

# Cursor
c = conn.cursor()

# Create tables

users_sql = '''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        PRIMARY KEY (username)
    );
'''

accounts_sql = '''
    CREATE TABLE IF NOT EXISTS accounts(
        account_number INTEGER,
        username TEXT,
        account_type TEXT,
        bank_name TEXT,
        routing_number INTEGER,
        PRIMARY KEY (account_number),
        FOREIGN KEY (username) REFERENCES users(username)
    );
'''

checking_sql = '''
    CREATE TABLE IF NOT EXISTS checking (
    account_number INTEGER,
    transaction_id INTEGER,
    date TEXT,
    description TEXT,
    payment_amt REAL,
    deposit_amt REAL,
    balance REAL,
    PRIMARY KEY (account_number, transaction_id),
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
    );
'''

# Drop tables if needed
# drop_users_sql = '''DROP TABLE IF EXISTS users'''
# drop_accounts_sql = '''DROP TABLE IF EXISTS accounts'''
# drop_checking_sql = '''DROP TABLE IF EXISTS checking'''
# c.execute(drop_users_sql)
# c.execute(drop_accounts_sql)
# c.execute(drop_checking_sql)


# Execute Queries
c.execute(users_sql)
c.execute(accounts_sql)
c.execute(checking_sql)

# Commit sql
conn.commit()

# Close connection
conn.close()