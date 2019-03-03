
import sqlite3 as a
con = a.connect("official tech.db")
cur = con.cursor()
cur.execute("insert into student values(555, 'nick', 785924)")
con.commit() # use use it when we insert/update delete
# commit function is used to save the modification done in table
con.close()