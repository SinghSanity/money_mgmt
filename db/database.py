'''File used to create database tables.'''
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
GLOBAL_DB = os.getenv('GLOBAL_DB')

def create_tables():
    '''Functionality to create tables'''
    # Connect to / Create  DB
    conn = sqlite3.connect(GLOBAL_DB)

    # Cursor
    c = conn.cursor()

    # Create tables
    users_sql = '''
        CREATE TABLE IF NOT EXISTS users(
            username TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            PRIMARY KEY (username)
        );
    '''

    bank_account_sql = '''
        CREATE TABLE IF NOT EXISTS bank_account(
            account_number TEXT NOT NULL UNIQUE,
            username TEXT,
            account_type TEXT NOT NULL,
            bank_name TEXT NOT NULL,
            routing_number TEXT NOT NULL,
            account_balance REAL DEFAULT 0,
            PRIMARY KEY (account_number),
            FOREIGN KEY (username) REFERENCES users(username)
        );
    '''

    checking_sql = '''
        CREATE TABLE IF NOT EXISTS checking (
        account_number TEXT NOT NULL,
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

    # Execute Queries
    c.execute(users_sql)
    c.execute(bank_account_sql)
    c.execute(checking_sql)

    # Commit sql
    conn.commit()

    # Close connection
    conn.close()

def delete_tables():
    '''Functionality to drop all tables if needed'''

    # Connect to / Create  DB
    conn = sqlite3.connect(GLOBAL_DB)

    # Cursor
    c = conn.cursor()
    drop_users_sql = '''DROP TABLE IF EXISTS users'''
    drop_bank_account_sql = '''DROP TABLE IF EXISTS bank_account'''
    drop_checking_sql = '''DROP TABLE IF EXISTS checking'''

    c.execute(drop_users_sql)
    c.execute(drop_bank_account_sql)
    c.execute(drop_checking_sql)

    # Commit sql
    conn.commit()

    # Close connection
    conn.close()
