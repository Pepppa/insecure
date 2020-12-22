import sqlite3
import sys

def start_db() :
    conn = sqlite3.connect("/home/admin/employee.db")
    return conn

def stop(conn) :
    conn.commit()
    conn.close()


def initialize_db() :
    try :
        conn = start_db()
        conn.cursor().execute('''CREATE TABLE employee (name text, phone_number text) ''')
        conn.cursor().execute('''INSERT INTO employee VALUES ('xshiolg', '+7 555 555 55 55') ''')
        conn.cursor().execute('''INSERT INTO employee VALUES ('kitty', '+7 555 111 11 11') ''')
        stop(conn)
    except:
        print("Unexpected error:",sys.exc_info()[0])

def get_info(username, infotype) :
    conn = start_db()
    sql = """ SELECT """ + infotype + """ FROM employee WHERE name LIKE '""" + username + """'"""
    print("Ready to run sql " + sql)
    try :
        result = conn.cursor().execute(sql).fetchall()
    except :
        result = str(sys.exc_info())
        print("Unexpected error:", result)
    stop(conn)
    print(result)
    return result


def get_available_fields() :
    conn = start_db()
    sql = "SELECT * FROM employee"
    columns = list(map(lambda x: x[0], conn.cursor().execute(sql).description))
    print(columns)
    stop(conn)
    return str(columns)
