
print("select one of given")
print(15*'=', 'Menu', 15*'=')
select = int(input("1.Add New Account\n2.View All Details\n3.Delete One\n4.Update One\n"))

import sqlite3 as s
c = s.connect("account_details.db")
cc = c.cursor()
#cc.execute("create table if not exists account (account_no number primary key, name text, pin number, balance real)")

if select == 1:
    ac_no = int(input("Account No: "))
    cc.execute("select * from account where account_no = ?", (ac_no, ))
    ck = cc.fetchone()

    if ck == None:
        nm = input("Name: ")
        pn = int(input("PIN: "))
        bal = float(input("BALANCE: "))
        #cc.execute("insert into account values(account_no, name, pin, balance)")
        cc.execute("insert into account values(?,?,?,?)", (ac_no, nm, pn, bal, ))
        c.commit()
        print("Account Created!")
    else:
        print("Account already available")

elif select == 2:
    # details
    ac_no = int(input("Account NO: "))
    cc.execute("select * from account where account_no = ?", (ac_no, ))
    ck = cc.fetchone()

    if ck == None:
        print("Account not found")
    else:
        cc.execute("select * from account where account_no = ?", (ac_no, ))
        print(cc.fetchall())

elif select == 3:
    ac_no = int(input("Account No: "))
    cc.execute("select * from account where account_no = ?", (ac_no, ))
    ck = cc.fetchone()

    if ck == None:
        print("Invalid Account!")
    else:
        cc.execute("delete from account where account_no = ?", (ac_no, ))
        c.commit()
        print("Account Deleted")

elif select == 4:
    ac_no = int(input("Account NO: "))
    cc.execute("select * from account where account_no = ?", (ac_no, ))
    ck = cc.fetchone()

    if ck:
        balance = float(input("New Balance: "))
        cc.execute("update account set balance = ? where account_no = ?", (balance, ac_no, ))
        c.commit()
        print("Updated!")
    else:
        print("Account Not Found!")
