import sqlite3

cursor.execute("""CREATE TABLE employee (name text, phone_number text)""")
cursor.execute("""INSERT INTO employee VALUES ('xshiolg', '+7 555 555 55 55') """)
cursor.execute("""INSERT INTO employee VALUES ('kitty', '+7 555 111 11 11')""")
conn.commit()

def start_db() :
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    return cursor

def commit(cursor) :
    conn.commit()


def initialize_db() :
    cursor = start_db()
    sql = """
    CREATE TABLE employee (name text, phone_number text)
    INSERT INTO employee VALUES ('xshiolg', '+7 555 555 55 55')
    INSERT INTO employee VALUES ('kitty', '+7 555 111 11 11')
    """
    cursor.execute(sql)
    commit(cursor)

def get_info(username, infotype) :
    cursor = start_db()
    sql = """
    SELECT * FROM employee WHERE name LIKE
     """ + username
    result = cursor.execute(sql)
    commit(cursor)
    print(result)
    return result


