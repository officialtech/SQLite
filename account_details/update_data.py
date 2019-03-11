
ac_no = int(input("Account No: "))
import sqlite3 as s
con = s.connect("account_details.db")
cur = con.cursor()
cur.execute("select * from account where account_no = ?", (ac_no, ))
res = cur.fetchall()
print(res)