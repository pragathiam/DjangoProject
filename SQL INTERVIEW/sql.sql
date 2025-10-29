import mysql.connector as mysql
con=mysql.connect(host="localhost",user='root',password='root',database='manoj')
cur=con.cursor()
query='create table emp(eno int,name varchar(20),salary int)'
cur.execute(query)
print('table created...!')
con.commit()
cur.close()
con.close()