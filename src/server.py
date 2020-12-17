from flask import *
import hashlib

from page_code import *
from passwd import *

app = Flask(__name__)

@app.route('/')
def index():
    login_url = url_for('first_login')
    return redirect(login_url)

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
            login_user_url = url_for('login', username = username, cookie = hash(password))
            return redirect(login_user_url)
    else:
        global login_form
        return in_body(login_form)

@app.route('/<username>', methods=['GET'])
def login(username) :
    print(request.args)
    pwd = request.args.getlist('cookie')[0]
    return in_body('''<p id="login" username="''' + username + '''" cookie="''' + pwd + '''"></p>''' + js('check_pwd'))

def read_script(js_name) :
    js_file = open(js_name)
    js_text = js_file.read()
    js_file.close()
    return js_text


@app.route('/check_pwd.js')
def check_pwd_js():
    return read_script("check_pwd.js")

@app.route('/admin.js')
def admin():
    return read_script("admin.js")

@app.route('/style.css')
def style_css():
    return read_script("style.css")


@app.route('/md5/<username>')
def get_passwd(username) :
    global shadow
    if username in shadow :
        return hash(shadow[username])
    else :
        return "No such user"

def hash(string) :
    return hashlib.md5(string.encode()).hexdigest()

app.run(host='0.0.0.0', port='5000')
