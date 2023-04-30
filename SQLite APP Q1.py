#Question 1
import sqlite3 
connection_obj = sqlite3.connect('test4.db')
crsr = connection_obj.cursor()
sql_command ="""CREATE TABLE IF NOT EXISTS Company (
  id int(11),
  name VARCHAR(255),
  description text,
  category_id int(11),
  chef_id int(255),
  created date);"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Company VALUES ("1","Paneer Tikka","Indian","1","BL000001","2000-13-23");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Company VALUES ("2","Pasta","Italian","2","BL000001","2005-11-23");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Company VALUES ("3","Pizza","Italian","2","BL000002","1999-11-23");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Company VALUES ("4","Noodles","Chinese","3","BL000002","2000-11-23");"""
crsr.execute(sql_command)
print("All Chinese Recipes")
crsr.execute("SELECT * FROM Company WHERE description = 'Chinese'")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
print("These are the Recipes prepared by the Chef BL000002")
crsr.execute("SELECT * FROM Company WHERE Chef_id = 'BL000002'")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
print("These are the Recipes starting with the Letter 'P'")

crsr.execute("SELECT * FROM Company WHERE name LIKE 'P%'")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
crsr.execute("SELECT * FROM Company ")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
crsr.execute("SELECT * FROM Company ORDER BY created")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
crsr.execute("UPDATE Company SET name='Momo' where id=1 ")
crsr.execute("SELECT * FROM Company ")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
crsr.execute("ALTER TABLE Company ADD C varchar(100)")
crsr.execute("UPDATE Company SET C='India' where id=1")
crsr.execute("SELECT * FROM Company ")
ans = crsr.fetchall()
for i in ans:print(i)
print("")
crsr.execute("delete from Company where id=1 ")
crsr.execute("SELECT * FROM Company ")
ans = crsr.fetchall()
for i in ans:print(i)

