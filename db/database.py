'''File used to create database tables.'''
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
GLOBAL_DB = os.getenv('GLOBAL_DB')

# Connect to / Create  DB
conn = sqlite3.connect(GLOBAL_DB)

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

BANK_ACCOUNT_SQL = '''
    CREATE TABLE IF NOT EXISTS bank_account(
        account_number INTEGER NOT NULL UNIQUE,
        username TEXT,
        account_type TEXT NOT NULL,
        bank_name TEXT NOT NULL,
        routing_number INTEGER NOT NULL,
        account_balance REAL DEFAULT 0,
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
    FOREIGN KEY (account_number) REFERENCES bank_account(account_number)
    );
'''

# Drop tables if needed
# DROP_USERS_SQL = '''DROP TABLE IF EXISTS users'''
# DROP_BANK_ACCOUNT_SQL = '''DROP TABLE IF EXISTS bank_account'''
# DROP_CHECKING_SQL = '''DROP TABLE IF EXISTS checking'''
# c.execute(DROP_USERS_SQL)
# c.execute(DROP_BANK_ACCOUNT_SQL)
# c.execute(DROP_CHECKING_SQL)


# Execute Queries
c.execute(USERS_SQL)
c.execute(BANK_ACCOUNT_SQL)
c.execute(CHECKING_SQL)

# Commit sql
conn.commit()

# Close connection
conn.close()
