n=int(input("Enter a number: "))
for d in range(2,n):
    if n%d==0:
        print(" Not a prime number")
        break
else:
    print("Prime Number")
