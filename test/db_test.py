# some_file.py
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/thelyolya/source/insecure/src/py')

import db

db.initialize_db("/home/thelyolya/source/insecure/test/test.db")

fields = db.get_available_fields_list()
signums = db.get_all_signums_list()

for user in signums:
    for field in fields:
        print(db.get_info(user, field))

print(db.get_info("demo", """ * FROM employee -- """))

