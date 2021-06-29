import hashlib

shadow = {
        'a.daniloff5': ("passw0rd", "+7 555 111 11 11", "Alex Danilov"),
        'alex': ("welcome", "+7 555 111 11 11", "Alexander of Macedon"),
        'testtest': ("princess", "+7 555 222 22 22", "Thorin Oakenshield"),
        'service': ("letmein", "+7 555 333 33 33", "Floki Vilgerdarson"),
        'sysadm': ("123456789", "+7 555 444 44 44", "Enakin Skywalker"),
        'orion': ("mera", "+7 555 555 55 55", "Jack \"Captain\" Sparrow"),
        'administrator': ("wpp_admin", "+7 555 666 66 66", "Jack Harkness"),
        'user1': ("starwars", "+7 555 777 77 77", "James Tiberius Kirk"),
        'testuser': ("abc123", "+7 555 888 88 88", "Daphne Bridgerton"),
        'vasya': ("qwerty", "+7 555 999 99 99", "Vasilii Terkin"),
        'demo': ("demo", "+7 555 000 00 00", "Sasha Zvereva")
        }

def hash(string) :
    return hashlib.md5(string.encode()).hexdigest()

def get_password(username):
    global shadow
    if username in shadow :
        (pwd, number, fullname) = shadow[username]
        return pwd
    else :
        return "No such user"

def get_password_hash(username):
    global shadow
    if username in shadow :
        (pwd, number, fullname) = shadow[username]
        return hash(pwd)
    else :
        return "No such user"

def get_all_usernames():
    global shadow
    return shadow.keys()

def get_telephone_number(username) :
    global shadow
    if username in shadow :
        (pwd, number, fullname) = shadow[username]
        return number
    else :
        return "No such user"

def get_fullname(username) :
    global shadow
    if username in shadow :
        (pwd, number, fullname) = shadow[username]
        return fullname
    else :
        return "No such user"

if __name__ == '__main__':
   for elem in shadow :
       print(elem + ":" + get_password(elem))

