# import mysql.connector as mysql
# con=mysql.connect(host="localhost",user='root',password='root',database='pragathi')
# cur=con.cursor()
# query='create table emp(eno int,name varchar(20),salary int)'
# cur.execute(query)
# print('table created...!')
# con.commit()
# cur.close()
# con.close() 



# import mysql.connector as myself 
# con=mysql.connect(user='root',password='root',host='localhost',database='pragathi')
# cur=con.cursor()
# name="mandu","indu"
# cur.execute(f'''select * from emp where name =any{name}''')
# print(cur.fetchall())
# cur.close()
# con.close()

import mysql.connector as myself 
con=mysql.connect(user='root',password='root',host='localhost',database='pragathi')
cur=con.cursor()
name=input('enter name:')
cur.execute(f'''select * from emp where name = {name}''')
print(cur.fetchall())
cur.close()
con.close()

