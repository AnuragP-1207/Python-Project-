def sum_natural(n):
    if(n==1):
        return 1
    else:
        return n+ sum_natural(n-1)
num=int(input("Enter stop value: "))
print("sum= ",sum_natural(num))
