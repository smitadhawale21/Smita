import sqlite3
from sqlite3.dbapi2 import Cursor
conn=sqlite3.connect('test.db')
c=conn.cursor()
conn.execute(''' DELETE FROM STUDENT ''')
c.execute('''
CREATE TABLE IF NOT EXISTS STUDENT(
    student_no INT(3),
    student TEXT(30),
    student_dob TEXT,
    student_doj TEXT
);''')
#c.execute(''' DROP TABLE STUDENT''')
print("created table sucessfully")

c.execute(''' INSERT INTO STUDENT VALUES(1, 'SMITA', '1997-12-21', '2020-01-01');''')
c.execute(''' INSERT INTO STUDENT VALUES(2, 'AKSHAY', '1997-04-06', '2019-08-15');''')
c.execute(''' INSERT INTO STUDENT VALUES(3, 'ARATI', '2000-12-25', '2021-05-13');''')
c.execute(''' INSERT INTO STUDENT VALUES(4, 'SAGAR', '1994-07-09', '2020-01-20');''')
c.execute(''' INSERT INTO STUDENT VALUES(5, 'BHARAT', '1994-04-17', '2018-05-08');''')
c.execute(''' INSERT INTO STUDENT VALUES(6, 'RUTUJA', '2001-02-06', '2020-05-24');''')
c.execute(''' SELECT * FROM STUDENT''')
results=c.fetchall()
print(results)
c.execute(''' DELETE FROM STUDENT WHERE STUDENT_NO=6; ''')
c.execute(''' UPDATE STUDENT SET STUDENT_NO='4' WHERE STUDENT_NO=3 ''')
c.execute(''' SELECT student FROM STUDENT ; ''')

conn.commit()
c.close()
conn.close()