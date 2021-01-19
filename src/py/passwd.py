import hashlib

shadow = {
        'sunny': ("qwerty", "+7 555 111 11 11"),
        'missy': ("1234", "+7 555 222 22 22")
        }

def hash(string) :
    return hashlib.md5(string.encode()).hexdigest()

def get_password(username):
    global shadow
    if username in shadow :
        (pwd, number) = shadow[username]
        return pwd
    else :
        return "No such user"

def get_password_hash(username):
    global shadow
    if username in shadow :
        (pwd, number) = shadow[username]
        return hash(pwd)
    else :
        return "No such user"

def get_all_usernames():
    global shadow
    return shadow.keys()

def get_telephone_number(username) :
    global shadow
    if username in shadow :
        (pwd, number) = shadow[username]
        return number
    else :
        return "No such user"

if __name__ == '__main__':
   for elem in shadow :
       print(elem + ":" + get_password(elem))

