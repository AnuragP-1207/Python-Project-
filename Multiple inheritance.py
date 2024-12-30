class Student():
   def getStudent(self):
      self.name=input("Enter Your Name: ")
      self.sno=input("Enter Your Seat no.: ")

class Exam():
   def getMarks(self):
      self.PP=int(input("Enter PP marks: "))
      self.AM=int(input("Enter AM marks: "))
      self.DS=int(input("Enter DS marks: "))
      self.DBMS=int(input("Enter DBMS marks: "))
      self.CN=int(input("Enter CN marks: "))

class Result(Student,Exam):
   def display(self):
      print("-----------------------------------------------------")
      print("Name: ",self.name)
      print("Exam seat no.: ",self.sno)
      self.total=self.PP+self.AM+self.DS+self.DBMS+self.CN
      print("Total : ",self.total)

s=Result()
s.getStudent()
s.getMarks()
s.display()
