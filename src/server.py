from flask import *

app = Flask(__name__)

login_form = '''
        <form method="post">
            <p><input type=text name=login>
            <p><input type=password name='password'>
            <p><input type=submit value=Login>
        </form>
        '''

def in_body(body = "") :
    return "<html><body>" + body + "</body></html>"

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
            return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        else:
            login_user_url = url_for('login', username = username, password = password)
            return redirect(login_user_url)
    else:
        global login_form
        return in_body(login_form)

@app.route('/login/<username>', methods=['GET'])
def login(username) :
    print(request.args)
    pwd = request.args.getlist('password')
    return '''
    <html><body>
    Login ''' + username + ''' with ''' + str(pwd) + '''...
    <script src="check_pwd.js"></script>
    </body></html>
    '''


@app.route('/login/check_pwd.js')
def check_pwd_js():
    check_pwd_file = open("check_pwd.js")
    check_pwd_text = check_pwd_file.read()
    check_pwd_file.close()
    return check_pwd_text


app.run(host='0.0.0.0', port='5000')
