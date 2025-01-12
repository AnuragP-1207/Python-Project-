list_num=[]
list_prime=[]

print("Enter 10 number:")
for i in range(10):
   n=int(input())
   list_num.append(n)
   p=True
   for d in range(2,n):
      if n%d==0:
         p=False
         break
   if p==True:
      list_prime.append(n)

print(list_prime)
print("list of prime number :")

         
