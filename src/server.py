from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        if request.form is None:
            abort(400)
        form = request.form
        if 'login' not in form or 'password' not in form:
            abort(400)

        login = form['login']
        password = form['password']
        if login == 'admin' and password == 'admin':
            return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        elif login == 'xshiolg' and password == '1408':
            return 'TOP SECRET'
        else:
            return abort(401)
    else:
        return '''
        <html><body>
        <form method="post">
            <p><input type=text name=login>
            <p><input type=password name='password'>
            <p><input type=submit value=Login>
        </form>
        <script src="check_pwd.js"></script>
        </body></html>
    '''

app.run(host='0.0.0.0', port='5000')
