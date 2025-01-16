list_num=[]
list_odd=[]
list_even=[]

print("Enter 10 numbers :")
for i in range(10):
   n=int(input())
   list_num.append(n)

for num in list_num:
   if num%2==0:
      list_even.append(num)
   else:
      list_odd.append(num)

print("\n list the odd numbers: ")
print(list_odd)


print("\n list the even number  : ")
print(list_even)





