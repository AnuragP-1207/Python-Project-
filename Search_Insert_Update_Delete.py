import mysql.connector as mysql
import tkinter
window = tkinter.Tk()
conn = mysql.connect(user = 'root',password = '12345',host = '127.0.0.1',db = 'mydb_b')
cursor = conn.cursor()
v1 = tkinter.StringVar()
eid = tkinter.StringVar()
ename = tkinter.StringVar()
age = tkinter.StringVar()
dept = tkinter.StringVar()
def clear():
    v1.set('')
    eid.set('')
    ename.set('')
    age.set('')
    dept.set('')
def search():
    sql = "SELECT * FROM employee WHERE emp_id = " +v1.get()+";"
    try:
        cursor.execute(sql)
        row = cursor.fetchone()
        if row == None:
            m = tkinter.messagebox.showinfo("Employee","No Record Found")
            v1.set('')
            eid.set('')
            ename.set('')
            age.set('')
            dept.set('')
        else:
            eid.set(row[0])
            ename.set(row[1])
            age.set(row[2])
            dept.set(row[3])
    except mysql.Error as err:
        print(err)
def save():
    sql = "INSERT INTO employee VALUES("+eid.get()+",'"+ename.get()+"',"+age.get()+",'"+dept.get()+"');"
    try:
        cursor.execute(sql)
        m = tkinter.messagebox.showinfo("Save","Record Saved Successfully")
        clear()
        conn.commit()
    except mysql.Error as err:
        print(err)
def update():
    if eid.get()=='':
        m = tkinter.messagebox.showinfo("Employee","Kindly enter Employee Id")
    else:
        ans = tkinter.messagebox.askyesno("Update","Save Changes?")
        if ans:
            sql = "UPDATE employee SET emp_name = '"+ ename.get()+"',emp_age = " + age.get() + ",dept_name = '" + dept.get() + "' WHERE emp_id = " + v1.get() + ";"
            try:
                cursor.execute(sql)
                m = tkinter.messagebox.showinfo("Update","Record Modified Successfully")
                clear()
                conn.commit()
            except mysql.Error as err:
                print(err)
def delete():
    if eid.get()=='':
        m = tkinter.messagebox.showinfo("Employee","Kindly enter Employee Id")
    else:
        ans = tkinter.messagebox.askyesno("Delete","Delete Record?")
        if ans:
            sql = "DELETE FROM employee WHERE emp_id = " + eid.get() + ";"
            try:
                cursor.execute(sql)
                m = tkinter.messagebox.showinfo("Delete","Record Deleted Successfully")
                clear()
                conn.commit()
            except mysql.Error as err:
                print(err)
                
L1 = tkinter.Label(window,text = "Enter Employee Id:").grid(row = 1,column = 1,sticky = 'w')
e1 = tkinter.Entry(window,width = 5,textvariable = v1).grid(row = 1,column = 2,sticky = 'w')
b1 = tkinter.Button(window,text = "Search",command = search).grid(row = 2,column = 1,columnspan = 2,padx = 10,pady = 10)

L2 = tkinter.Label(window,text = "Employee Id:").grid(row = 3,column = 1,sticky = 'w')
L3 = tkinter.Label(window,text = "Employee Name:").grid(row = 4,column = 1,sticky = 'w')
L4 = tkinter.Label(window,text = "Age:").grid(row = 5,column = 1,sticky = 'w')
L5 = tkinter.Label(window,text = "Department:").grid(row = 6,column = 1,sticky = 'w')

e_id = tkinter.Entry(window,textvariable = eid).grid(row = 3,column = 2,sticky = 'w')
e_name = tkinter.Entry(window,textvariable = ename).grid(row = 4,column = 2,sticky = 'w')
e_age = tkinter.Entry(window,textvariable = age).grid(row = 5,column = 2,sticky = 'w')
e_dept = tkinter.Entry(window,textvariable = dept).grid(row = 6,column = 2,sticky = 'w')

b2 = tkinter.Button(window,text = "Save",command = save).grid(row = 7,column = 1,padx = 10,pady = 10)
b3 = tkinter.Button(window,text = "Update",command = update).grid(row = 7,column = 2,sticky = 'w',padx = 10,pady = 10)
b4 = tkinter.Button(window,text = "Delete",command = delete).grid(row = 7,column = 2,sticky = 'e',padx = 10,pady = 10)
window.mainloop()
conn.close()
