from flask import *
import sys
import re

from page_code import *
from passwd import hash

import db

db.open("/home/admin/employee.db")

app = Flask(__name__)

@app.route('/')
def index():
    login_url = url_for('first_login')
    return redirect(login_url)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/login', methods=['GET', 'POST'])
def first_login():
    if request.method == 'POST':
        if request.form is None:
            abort(400)
        form = request.form
        if 'login' not in form :
            abort(400)

        username = form['login']
        if 'password' in form :
            password = form['password']
        else :
            password = ""

        if username == 'admin' and password == 'admin':
            return in_body(js('admin'))

        else:
            log("Handle login " + username + " with password " + password)
            login_user_url = url_for('login', username = username, cookie = hash(password))
            return redirect(login_user_url)
    else:
        global login_form
        return in_body(login_form)

@app.route('/<username>', methods=['GET', 'POST'])
def login(username) :
    pwd = request.args.getlist('cookie')[0]
    if request.method == 'POST':
        form = request.form
        try:
            if 'field' in form :
                search_text = form['field']
                if re.search(r'DROP TABLE|DELETE FROM', search_text, re.IGNORECASE) :
                    return in_body(js('drop'))
                else :
                    return in_body(lk("lk", username, pwd, db.get_available_fields(), found_result(username, search_text)) + js('check_pwd'))
            else:
                return in_body(lk("lk", username, pwd, db.get_available_fields()) + js('check_pwd'))
        except:
            print("Database call is failed. Details: " +  str(sys.exc_info()) + "type " + str(type(sys.exc_info())))
            main_text = "Something went wrong while proceeding with the request. Please send bug report to support: "
            (class_name, db_error_object, traced_object) = sys.exc_info()
            report_button = bug_report(str(db_error_object).replace('<', '&lt').replace('>', '&gt'))
            return in_body(lk("lk", username, pwd, db.get_available_fields(), main_text, report_button) + js('check_pwd'))
    else:
        print("My method is get")
        print("Login " + username + " with " + str(request.args))
        return in_body(lk("login", username, pwd, db.get_available_fields()) + js('check_pwd'))


def log(log_entry) :
    with open('/var/log/security_events.log', 'a') as the_file:
        the_file.write(log_entry + '\n')

def found_result(username, text) :
    return text + " found for user " + username + ": " + str(db.get_info(username, text))

app.run(host='0.0.0.0', port='5000')
