
idno = int(input("ID NO "))
name = input("NAME ")
contact = int(input("CONTACT "))

import sqlite3 as s
con = s.connect("official tech.db")
print("Connection establized!")
cr = con.cursor() # to perform operation we use cursor object
cr.execute("insert into student values(?,?,?)",(idno, name, contact))
con.commit() # save
con.close()