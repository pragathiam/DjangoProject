# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''CREATE TABLE IF NOT EXISTS emp(eid integer PRIMARY KEY,name text,age integer,salary real)''')
# print('table created successfully')
# cur.close()
# con.close()

# inserting records
# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''insert into emp values(1,'indu',16,10000)''')
# cur.execute('''insert into emp values(2,'manu',20,2000)''')
# cur.execute('''insert into emp values(3,'areeba',22,30000)''')
# con.commit()
# print('records inserted successfully')
# cur.close()
# con.close()

# #multiple records
# import  sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# query='insert into emp values(?,?,?,?)'
# data=[(4,'sana',25,40000),(5,'sara',30,50000),(6,'dana',35,60000)]
# cur.executemany(query,data)
# con.commit()
# print('data inserted successfully')
# cur.close()
# con.close()

#Fetching Records
# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''select * from emp''')
# rows=cur.fetchall()
# #print(rows)
# for row in rows:
#     print(*row)
# cur.close()
# con.close()

# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''select * from emp where age>20''')
# rows=cur.fetchall()
# for row in rows:
#     print(*rows)
# cur.close()
# con.close()

# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''select * from emp where age>20''')
# res=cur.fetchone()
# print(res)
# cur.close()
# con.close()

# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute('''select * from emp where age>20''')
# rows=cur.fetchmany(3)
# for row in rows:
#     print(*row)
# cur.close()
# con.close()


# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# age=int(input('Enter age:'))
# res=cur.execute(f'''select * from emp where age>{age}''')
# print(res.fetchall())
# cur.close()
# con.close()


#20% increment
# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute("SELECT SALARY,SALARY * 1.20  FROM EMP")
# rows = cur.fetchall()
# for row in rows:
#     print(f"Original Salary: {row[0]}, Incremented Salary: {row[1]}")
# cur.close()
# con.close()


#15% decrement<=24
# import sqlite3 as db
# con=db.connect('employee.db')
# cur=con.cursor()
# cur.execute("SELECT SALARY,SALARY * 0.85 FROM EMP WHERE SALARY<=24")
# rows = cur.fetchall()
# for row in rows:
#     print(f"Original Salary: {row[0]}, After 15% Decrement: {row[1]}")
# cur.close()
# con.close()


# 1.SID NAME MARKS 10 STUDENT RECORD
import sqlite3 as db
con=db.connect('student.db')
cur=con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS std(sid integer PRIMARY KEY,name text,age integer,marks real)''')
print('table created successfully')
cur.close()
con.close()


import sqlite3 as db
con=db.connect('student.db')
cur=con.cursor()
query='insert into values(?,?,?)'
data= [(1, 'AB', 100),(2, 'AC', 92),(3, 'AD', 76),(4, 'AE', 88),(5, 'AF', 67),(6, 'AG', 95),(7, 'AH', 73),(8, 'AI', 81),(9, 'AJ', 90),(10, 'AK', 78)]
cur.executemany(query,data)
con.commit()
print("data inserted successfully")
cur.close()
con.close()




# 2.ALTER STUDENT TABLE ADD GRADE

# 3.UPDATE STUDENT GRADE SINGLE QUERY