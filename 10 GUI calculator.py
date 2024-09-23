import tkinter
window=tkinter.Tk()
window.title("Calculator")
window.geometry("200x100")

n1=tkinter.IntVar()
n2=tkinter.IntVar()
res=tkinter.StringVar()

def add():
   r=n1.get()+n2.get()
   res.set(r)

def sub():
   r=n1.get()-n2.get()
   res.set(r)

def mul():
   r=n1.get()*n2.get()
   res.set(r)

def div():
   r=n1.get()/n2.get()
   res.set(r)

l1=tkinter.Label(window,text="Number 1 : ").grid(row=1,column=1, sticky="w")
e1=tkinter.Entry(window,textvariable=n1).grid(row=1,column=2,columnspan=3,sticky="w")
l2=tkinter.Label(window,text="Number 2 : ").grid(row=2,column=1,sticky="w")
e2=tkinter.Entry(window,textvariable=n2).grid(row=2,column=2,columnspan=3,sticky="w")
l3=tkinter.Label(window,text="Result : ").grid(row=3,column=1,sticky="w")
e3=tkinter.Entry(window,textvariable=res).grid(row=3,column=2,columnspan=3,sticky="w")

b_add=tkinter.Button(window,text="+",command=add).grid(row=4,column=1,padx=10,pady=10)
b_sub=tkinter.Button(window,text="-",command=sub).grid(row=4,column=2,padx=10,pady=10)
b_mul=tkinter.Button(window,text="*",command=mul).grid(row=4,column=3,padx=10,pady=10)
b_div=tkinter.Button(window,text="/",command=div).grid(row=4,column=4,padx=10,pady=10)

window.mainloop()
