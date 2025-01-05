sub={'s1':"PP",'s2':"CN",'s3':"DS",'s4':"DBMS",'s5':"AM/MP"}
print(sorted(sub.items()))
print(sorted(sub.items(),reverse=True))

temp={}
for k,v in sub.items():
   temp.update({v:k})

print("\n Dictionary in ascending order of value: ")
for k,v in sorted(temp.items()):
   print("{}:{}".format(v,k))

print("\n Dictionary in descending order of value: ")
for k,v in sorted(temp.items(),reverse=True):
   print("{}:{}".format(v,k))   
