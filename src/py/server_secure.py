from flask import *
from flask_cors import CORS
from passwd import *

app = Flask(__name__)
CORS(app)

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
