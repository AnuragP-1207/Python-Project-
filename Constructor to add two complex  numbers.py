class complex_num():
   def __init__(self,c1,c2):
      self.c1=c1
      self.c2=c2
   def sum(self):
      s=self.c1+self.c2
      print("Sum= ",s)

print("x1 and y1 values for the given complex number1: ")
x1,y1=map(int,input().split())
c1=complex(x1,y1)
print("x2 and y2 values for the given complex number1: ")
x2,y2=map(int,input().split())
c2=complex(x2,y2)
c=complex_num(c1,c2)
c.sum()
