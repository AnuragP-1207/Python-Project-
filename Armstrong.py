##def armstrong(n):
##    s=0
##    temp=n
##    p=len(str(n))
##    while(temp!=0):
##        digit=temp%10
##        s+=digit**p
##        temp//=10
##    if(s==n):
##        print(n,"is an armstrong number")
##    else:
##        print(n,"is not an armstrong number")
##num=int(input("Enter a number:"))
##armstrong(num)

##def reverse(n):
##    rev = 0
##    while (n!=0):
##        rev = (rev*10)+(n%10)
##        n//=10
##    return rev
##
##num = int(input("Enter the no.: "))
##print("Reverse no.: ",num,"=",reverse(num))
##

##def palin(n):
##    temp = n
##    s = 0
##    while(temp!=0):
##        rem = temp%10
##        s= rem+(s*10)
##        temp//=10
##    if(s==n):
##        print(n,"is a plin")
##    else:
##        print(n,"not palin")
##
##num = int(input("Enter the no.: "))
##palin(num)




def cube(n):
    while(n>=0):
        digit=30%10
        s=n**digit
        break
num = int(input("Enter the no.: "))
print("Cube: ",num,"=",cube(num))
