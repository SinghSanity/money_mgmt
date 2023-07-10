'''Functionality for users'''
import sqlite3
from db.utils import select_helper

def get_users():
    '''Returns a list of all usernames currently available'''
    user_list = select_helper(attributes=['username'], table='users')
    user_list = [item[0] for item in user_list]
    return user_list

def add_user(username, first_name, last_name):
    '''Add a user to the database'''
    try:
        user_list = get_users()
        if username in user_list:
            raise Exception("This username is already in the table. Please use a different one.")
        if not first_name or not last_name:
            raise Exception("First Name or Last Name is not provided.")

        s_sql = '''
            INSERT INTO users (username, first_name, last_name)
            VALUES('{0}', '{1}', '{2}');
        '''.format(str(username), str(first_name), str(last_name))

        conn = sqlite3.connect('money.db')
        c = conn.cursor()

        print("Executing query: " + s_sql)

        c.execute(s_sql)
        conn.commit()
        conn.close()
        print("Successfully added user to the table.")
    except Exception as e:
        print("Caught this exception: " + str(e))

def remove_user(username):
    '''Remove a user from the database'''
    try:
        user_list = get_users()
        if not username in user_list:
            raise Exception("This username does not exist in the table.")

        s_sql = '''
            DELETE FROM users
            WHERE username = '{0}';
        '''.format(str(username))

        conn = sqlite3.connect('money.db')
        c = conn.cursor()

        print("Executing query: " + s_sql)

        c.execute(s_sql)
        conn.commit()
        conn.close()
        print("Successfully removed user from the table.")
    except Exception as e:
        print("Caught this exception: " + str(e))

if __name__ == '__main__':
    pass
    # print(get_users())
    # set_user('username', 'First_Name', 'Last_Name')
    # remove_user(username='username')
