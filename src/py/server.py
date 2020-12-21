from flask import *

from page_code import *
from passwd import hash
from db import *

app = Flask(__name__)
db.initialize_db()

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
        if 'field' in form :
            search_text = form['field']
            return in_body(lk("lk", username, pwd, found_result(username, search_text)) + js('check_pwd'))
        else:
            return in_body(lk("lk", username, pwd) + js('check_pwd'))
    else:
        print("My method is get")
        print("Login " + username + " with " + str(request.args))
        return in_body(lk("login", username, pwd) + js('check_pwd'))


def log(log_entry) :
    with open('/home/admin/security.log', 'a') as the_file:
        the_file.write(log_entry + '\n')

def found_result(username, text) :
    return "For " + text + " found " + db.get_info(username, text)

app.run(host='0.0.0.0', port='5000')
