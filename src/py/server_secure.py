from flask import *

from passwd import *

app = Flask(__name__)

@app.route('/')
def index():
    return "404"

@app.route('/md5/<username>')
def get_passwd(username) :
    global shadow
    if username in shadow :
        return hash(shadow[username])
    else :
        return "No such user"

app.run(host='0.0.0.0', port='5001')
