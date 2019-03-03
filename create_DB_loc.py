
# connect function will take one parameter that is DB file name
# connect function will search for given DB file name, if file not exists
# create a new file and get the DB connection
# if file available, just make connection

import sqlite3 as s
c = s.connect(r"C:\Users\official-tech\Desktop\official.sqlite") # extentions .db and .sqlite
print(c)

# connect function will return the Connect object