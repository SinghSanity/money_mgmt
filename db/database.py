'''File used to create database tables.'''
import sqlite3

# Connect to / Create  DB
conn = sqlite3.connect('money.db')

# Cursor
c = conn.cursor()

# Create tables

USERS_SQL = '''
    CREATE TABLE IF NOT EXISTS users(
        username TEXT NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        PRIMARY KEY (username)
    );
'''

ACCOUNTS_SQL = '''
    CREATE TABLE IF NOT EXISTS accounts(
        account_number INTEGER NOT NULL UNIQUE,
        username TEXT,
        account_type TEXT NOT NULL,
        bank_name TEXT NOT NULL,
        routing_number INTEGER NOT NULL,
        PRIMARY KEY (account_number),
        FOREIGN KEY (username) REFERENCES users(username)
    );
'''

CHECKING_SQL = '''
    CREATE TABLE IF NOT EXISTS checking (
    account_number INTEGER NOT NULL,
    transaction_id INTEGER,
    date TEXT NOT NULL,
    description TEXT,
    payment_amt REAL NOT NULL DEFAULT 0,
    deposit_amt REAL NOT NULL DEFAULT 0,
    balance REAL NOT NULL DEFAULT 0,
    PRIMARY KEY (account_number, transaction_id),
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
    );
'''

# Drop tables if needed
# DROP_USERS_SQL = '''DROP TABLE IF EXISTS users'''
# DROP_ACCOUNTS_SQL = '''DROP TABLE IF EXISTS accounts'''
# DROP_CHECKING_SQL = '''DROP TABLE IF EXISTS checking'''
# c.execute(DROP_USERS_SQL)
# c.execute(DROP_ACCOUNTS_SQL)
# c.execute(DROP_CHECKING_SQL)


# Execute Queries
c.execute(USERS_SQL)
c.execute(ACCOUNTS_SQL)
c.execute(CHECKING_SQL)

# Commit sql
conn.commit()

# Close connection
conn.close()
