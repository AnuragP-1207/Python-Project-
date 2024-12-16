print("108")
##import mysql.connector as mysql
##conn=mysql.connect(user="root",password="12345",host='127.0.0.1')
##cursor=conn.cursor()
##try:
##    cursor.execute("create database mydb_b")
##except mysql.Error as err:
##    print("Error in creating database\n"+str(err))
##conn.close()
    
import mysql.connector as mysql
conn=mysql.connect(user='root',password="12345",host='127.0.0.1',db='mydb_b')
cursor=conn.cursor()
cursor.execute("select * from employee")
row=cursor.fetchone()
print(row)
rows=cursor.fetchmany(2)
print(rows)
rem_rows=cursor.fetchall()
print(rem_rows)
print("Total number of rows=",cursor.rowcount)
print("----------------------")
for r in rem_rows:
    print(r)
print("----------------------")
cursor.execute("select * from employee")
all_rows=cursor.fetchall()
for r in all_rows:
    print("Emp ID:",r[0])
    print("Emp Name:",r[1])
    print("Age:",r[2])
    print("Dept:",r[3])
    print("**********")
conn.close()


