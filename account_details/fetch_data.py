
import sqlite3 as a
con = a.connect("account_details.db")
cr = con.cursor()

ac_no = int(input("Account No: "))
cr.execute("select * from account where account_no = ?", (ac_no,))
ck = cr.fetchone()
print(ck)