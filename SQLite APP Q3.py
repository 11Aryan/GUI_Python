#Question 3
import sqlite3
connection= sqlite3.connect("mytable3.db")
crsr=connection.cursor()
connection.execute("PRAGMA foreign_keys = ON")
sql_command="""CREATE TABLE IF NOT EXISTS Product(
ID VARCHAR(255) PRIMARY KEY,
Prod_name VARCHAR(255),
Supplier_id VARCHAR(255),
Unit_price INT,
Package INT,
Order_ID VARCHAR(255)
);"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO Product VALUES('id001','pid001','001','1000','500','Oid001');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO Product VALUES('id002','pid002','002','2000','600','Oid002');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO Product VALUES('id003','pid003','003','3000','700','Oid003');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO Product VALUES('id004','pid004','004','4000','800','Oid004');"""
crsr.execute(sql_command)
sql_command="""CREATE TABLE IF NOT EXISTS OrderItem(
  ID VARCHAR(255),
  Order_id VARCHAR(255),
  Product_ID VARCHAR(255),
  Unit_price INT ,
  Quantity INT,
  FOREIGN KEY (ID) REFERENCES Product(ID)
  );"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO OrderItem VALUES('id001','oid001','pid001','1000','100');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO OrderItem VALUES('id002','oid002','pid002','2000','200');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO OrderItem VALUES('id003','oid003','pid003','3000','300');"""
crsr.execute(sql_command)
sql_command="""INSERT OR IGNORE INTO OrderItem VALUES('id004','oid004','pid004','4000','400');"""
crsr.execute(sql_command)
print("Displaying total quantity of each Product")
ans=crsr.execute("SELECT Quantity FROM OrderItem where ID = 'id001'")
for i in ans:print(i)
ans=crsr.execute("SELECT Quantity FROM OrderItem where ID = 'id002'")
for i in ans:print(i)
ans=crsr.execute("SELECT Quantity FROM OrderItem where ID = 'id003'")
for i in ans:print(i)
ans=crsr.execute("SELECT Quantity FROM OrderItem where ID = 'id004'")
for i in ans:print(i)
print("")
print("Displayin Unit price based on Supply id")
ans=crsr.execute("SELECT Unit_price FROM Product")
for i in ans:
  print(i)
print("")
print("Displaying Product name along with order id and supplier id")
ans=crsr.execute("SELECT Prod_name ,Order_ID ,Supplier_id FROM Product")
for i in ans:
  print(i)
connection.close()
