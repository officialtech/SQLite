
import sqlite3 as sql # importing module
conn_ion = sql.connect("account_details.db") # getting connection
cur_or = conn_ion.cursor() # creating cursor object

a_n  = int(input("Account Number: ")) # taking input to check if acc. is available or not
cur_or.execute("select * from account where account_no = ?", (a_n, )) # getting account
gt_data = cur_or.fetchone()

if gt_data == None:
    print("Account Number Not Found!")
else:
    cur_or.execute("delete from account where account_no = ?", (a_n, ))
    conn_ion.commit()
    print("Account Deleted!")