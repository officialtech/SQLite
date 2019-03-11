


import sqlite3 as s
connection_object = s.connect("account_details.db")
cursor_object = connection_object.cursor()
#cursor_object.execute("create table if not exists account(account_no number primary key, name text, pin number, balance real) ")

cursor_object.execute("insert into account values(100, 'the kiddies', 5685, 11100.00)")
#cursor_object.execute("select * from account")
#get_all_data = cursor_object.fetchall()
#print(get_all_data)
connection_object.commit()