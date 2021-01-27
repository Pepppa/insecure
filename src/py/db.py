import sqlite3
import sys
import passwd
import traceback

db_path = ""

class DbError(Exception):
    def __init__(self, details):
        self.details = details
        super().__init__(self.details)


def start_db() :
    global db_path
    print("Trying to connect to " + db_path)
    conn = sqlite3.connect(db_path)
    return conn

def stop(conn) :
    conn.commit()
    conn.close()

def open(path) :
    global db_path
    db_path = path
    try :
        conn = start_db()
        print("DB is connected")
        print("Available users:")
        print(get_all_signums_list())
        stop(conn)
    except:
        print("Unexpected error:",sys.exc_info())


def initialize_db(path) :
    global db_path
    db_path = path
    try :
        conn = start_db()
        print("Clean-up DB")
        conn.execute("DROP TABLE IF EXISTS employee")
        print("Create table")
        conn.cursor().execute('''CREATE TABLE employee (signum text, fullname text, phone_number text) ''')
        for employee in passwd.get_all_usernames() :
            print("""INSERT INTO employee VALUES ('""" + employee + """', '""" + passwd.get_telephone_number(employee)+ """') """)
            conn.cursor().execute("""INSERT INTO employee VALUES ('""" + employee + """', '""" + passwd.get_fullname(employee)+  """', '""" + passwd.get_telephone_number(employee)+ """') """)
        stop(conn)
    except:
        print("Unexpected error:",sys.exc_info())

def get_info(username, infotype) :
    conn = start_db()
    sql = """ SELECT """ + infotype + """ FROM employee WHERE signum LIKE '""" + username + """'"""
    print("Ready to run sql " + sql)
    try :
        result = conn.cursor().execute(sql).fetchall()
        print("Got good result: ", result)
        finish = []
        for item in result :
            finish.append(" ".join(list(item)))
        return ", ".join(finish)
    except :
        print("Unexpected error:")
        stop(conn)
        traceback.print_exc()
        raise DbError("SQLite request " + sql + " failed with exception " + traceback.format_exc().replace('''"''', ''' '''))


def get_available_fields_list() :
    conn = start_db()
    sql = "SELECT * FROM employee"
    columns = list(map(lambda x: x[0], conn.cursor().execute(sql).description))
    print(columns)
    stop(conn)
    return columns

def get_available_fields() :
    return ", ".join(get_available_fields_list())


def get_all_signums_list() :
    conn = start_db()
    sql = """ SELECT signum FROM employee """
    result = conn.cursor().execute(sql).fetchall()
    print("Result: ", result)
    finish = []
    for item in result :
        finish.append(", ".join(list(item)))
    return finish

def get_all_signums() :
    return ", ".join(get_all_signums_list())

