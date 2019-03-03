
import sqlite3 as s
conn = s.connect("official tech.db")
c = conn.cursor()
c.execute("create table student(id number primary key, name text, contact number)")

conn.close()