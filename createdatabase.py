import mysql.connector as mysql
conn=mysql.connect(user = "root", password = '12345', host = '127.0.0.1')
cursor=conn.cursor()
try:
    cursor.execute("CREATE DATABASE myDB_B")
except mysql.Error as err:
    print('Error in Creating Database\n'+str(err))
conn.close()
