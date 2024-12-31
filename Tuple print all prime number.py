t=(100,20,45,63,74,4634,5783,2434)
for n in  t:
   p=True
   for d in range(2,n):
         if(d%n==0):
          p=False
          break
         if p==True:
          print(n)
          break
