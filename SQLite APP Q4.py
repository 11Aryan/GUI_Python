import sqlite3
connection_obj = sqlite3.connect('mytable4.db')
crsr = connection_obj.cursor()
sql_command = """CREATE TABLE IF NOT EXISTS Job(
  job_id VARCHAR(255),
  job_title VARCHAR(255),
  Min_salary INT,
  Max_salary INT);"""
crsr.execute(sql_command)
sql_command = ("""INSERT INTO Job VALUES ("sd10ab","Senior Developer","1500000","2500000");""")
crsr.execute(sql_command)
sql_command = """INSERT INTO Job VALUES ("fed20xy","Front end Developer","1300000","2000000");"""
crsr.execute(sql_command)
sql_command = """INSERT INTO Job VALUES ("bed30yz","Back end Developer","1100000","2300000");"""
crsr.execute(sql_command)
crsr.execute("SELECT * FROM Job")
ans = crsr.fetchall()
for i in ans:
  print(i)
