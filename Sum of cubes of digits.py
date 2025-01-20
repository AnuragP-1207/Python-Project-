n=int(input("Enter a number: "))
s=0
temp=n
if(temp!=0):
    rem=temp%10
    s+=rem**3
    temp//=10
print("Sum of cubes of digits of {}={}".format(n,s))    
