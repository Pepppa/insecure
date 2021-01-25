import sqlite3
import sys
import passwd

class DbError(Exception):
    def __init__(self, details):
        self.details = details
        super().__init__(self.details)


def start_db() :
    print("Trying to connect to /home/admin/employee.db")
    conn = sqlite3.connect("/home/admin/employee.db")
    return conn

def stop(conn) :
    conn.commit()
    conn.close()


def initialize_db() :
    try :
        conn = start_db()
        print("Clean-up DB")
        conn.execute("DROP TABLE IF EXISTS employee")
        print("Create table")
        conn.cursor().execute('''CREATE TABLE employee (name text, phone_number text) ''')
        for employee in passwd.get_all_usernames() :
            print("""INSERT INTO employee VALUES ('""" + employee + """', '""" + passwd.get_telephone_number(employee)+ """') """)
            conn.cursor().execute("""INSERT INTO employee VALUES ('""" + employee + """', '""" + passwd.get_telephone_number(employee)+ """') """)
        stop(conn)
    except:
        print("Unexpected error:",sys.exc_info())

def get_info(username, infotype) :
    conn = start_db()
    sql = """ SELECT """ + infotype + """ FROM employee WHERE name LIKE '""" + username + """'"""
    print("Ready to run sql " + sql)
    try :
        result = conn.cursor().execute(sql).fetchall()
        print("Got good result: ", result)
        return result
    except :
        exception_details = str(sys.exc_info())
        print("Unexpected error:", exception_details)
        stop(conn)
        raise DbError("SQLite request\n" + sql + "\nfailed with exception:\n" + exception_details)


def get_available_fields() :
    conn = start_db()
    sql = "SELECT * FROM employee"
    columns = list(map(lambda x: x[0], conn.cursor().execute(sql).description))
    print(columns)
    stop(conn)
    return str(columns)
