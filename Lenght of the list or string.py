def count(s):
   len=0
   for c in s:
      len+=1
   return len

str=input("enter the string: ")
print("Lenght of the string:",count(str))
print("Length=",count(list(str)))
l1=[10,20,30]
print("length of the list: ",count(l1))
