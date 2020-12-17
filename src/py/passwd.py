import hashlib

shadow = {
        'xshiolg': "qwerty",
        'kitty': "1234"
        }

def hash(string) :
    return hashlib.md5(string.encode()).hexdigest()

for elem in shadow :
    print(elem + ":" + shadow[elem])
