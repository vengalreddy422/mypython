#Program for Reading Student Values and Display Values
# by Using Classes and Objects
#InstanceMethodEx3.py
class Student:
    def readstudvals(self,objinfo):
        print("-" * 50)
        print("Enter {} Student Information".format(objinfo))
        print("-"*50)
        self.sno=int(input("\tEnter Student Number:"))
        self.name=input("\tEnter Student Name:")
        self.marks=float(input("\tEnter Student Marks:"))
        print("-" * 50)
    def dispstudvals(self,objinfo):
        print("-" * 50)
        print("{} Student Information".format(objinfo))
        print("-" * 50)
        print("\tStudent Number:{}".format(self.sno))
        print("\tStudent Name:{}".format(self.name))
        print("\tStudent Marks:{}".format(self.marks))
        print("-" * 50)
#Main Program
#Create Two Objects of Student Class
s1=Student()
s2=Student()
#read  and display the Values for object s1 by using Instance Method
s1.readstudvals("First") # Calling Instance Methods by using Object Name
s1.dispstudvals("First")
#read and display the Values for object s2 by using Instance Method
s2.readstudvals("Second") # Calling Instance Methods by using Object Name
s2.dispstudvals("Second")
