def reverse(n):
    rev=0
    while(n!=0):
        rev=(rev*10)+n(n%10)
        n//=10
    return rev    
num=int(input("Enter a number: "))
print("Reverse of",num,"=",reverse(num))        
