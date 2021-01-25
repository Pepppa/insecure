import hashlib

shadow = {
        'olga.shilyagina': ("1q2w3e4r", "+7 555 111 11 11"),
        'testtest': ("iloveyou", "+7 555 222 22 22"),
        'service': ("letmein", "+7 555 333 33 33"),
        'sysadm': ("123456789", "+7 555 444 44 44"),
        'orioninc': ("mera", "+7 555 555 55 55"),
        'administrator': ("wpp_admin", "+7 555 666 66 66"),
        'user1': ("starwars", "+7 555 777 77 77"),
        'testuser': ("123qwe", "+7 555 888 88 88"),
        'alex': ("888888", "+7 555 999 99 99"),
        'demo': ("demo", "+7 555 000 00 00")
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

