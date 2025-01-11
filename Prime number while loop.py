n=int(input("Enter a Number:"))
d=2
while(d<n):
    if n%d==0:
        print("Not a Number")
        break
    else:
        d+=1
else:
    print("Prime number")
    
        
