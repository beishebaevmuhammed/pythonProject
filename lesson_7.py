import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

sql_to_create_employees_table = '''
CREATE TABLE employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    salary FLOAT NOT NULL DEFAULT 0.0,
    hobby TEXT DEFAULT NULL,
    birth_day DATE NOT NULL,
    is_married BOOLEAN DEFAULT FALSE
)
'''

connection = create_connection('gr36-1.db')
if connection is not None:
    print('Successfully connected to DB!')
    create_table(connection, sql_to_create_employees_table)
    connection.close()

