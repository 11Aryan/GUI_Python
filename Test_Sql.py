import sqlite3 
#connection_obj = sqlite3.connect('test4.db')
#crsr = connection_obj.cursor()
CREATE TABLE IF NOT EXISTS Company (
  id int(11),
  name VARCHAR(255),
  description text,
  category_id int(11),
  chef_id int(255),
  created datetime);
#crsr.execute(sql_command)
INSERT INTO Company VALUES ("1","Paneer Tikka","Indian","1","BL000001","1/1/2002");
select * from Ccompany;
