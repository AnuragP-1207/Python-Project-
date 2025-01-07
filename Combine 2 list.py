f1=open("1.txt","r")
f2=open("2.txt","r")
content1=f1.readlines()
content2=f2.readlines()
new_content=content1+content2
print(new_content)
f1.close()
f2.close()
