def compare(l1,l2):
   for i in l1:
      if (i in l2):
         return true
      break
   else:
      false

print("\n Enter 5 values in a list: ")
n1=[]
for i in range(5):
   n1.append(input())

print("\n Enter 5 values in a list: ")
n2=[]
for i in range(5):
   n2.append(input())

if compare(n1,n2):
   print("\n list is containning comman elements")
else:
   print(" dose not contain comman elements")
