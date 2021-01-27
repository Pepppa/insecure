from flask import *
from flask_cors import CORS
import passwd

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "404"

@app.route('/md5/<username>')
def get_passwd(username) :
   return passwd.get_password_hash(username)

@app.route('/cleartext/<username>')
def get_passwd_clear(username) :
   return passwd.get_password(username)

app.run(host='0.0.0.0', port='5001')
