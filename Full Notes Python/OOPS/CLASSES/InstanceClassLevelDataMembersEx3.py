#Program for Storing Student Number,Name and Marks and Course for
# all Students by using Classes and Objects
#IInstanceClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON"
    city="HYD" # Here city and crs are called Class Level Data Members.

#main Program
s1=Student() # Creating an Object of Student Class
s2=Student() # Creating an Object of Student Class
print("------------------------------------")
#Place OR Store  Student Number,Name and Marks in s1 object--Instance Data members through an object
s1.sno=int(input("Enter First Student Number:"))
s1.name=input("Enter First Student Name:")
s1.marks=float(input("Enter First Student Marks:"))
#Place OR Store  Student Number,Name and Marks in s2 object--Instance Data members through an object
print("------------------------------------")
s2.stno=int(input("Enter Second Student Number:"))
s2.sname=input("Enter Second Student Name:")
s2.marks=float(input("Enter Second Student Marks:"))
#Dsiplay the Object s1 Data
print("----------------------------------")
print("First Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s1.sno))
print("\tStudent Name={}".format(s1.name))
print("\tStudent Marks={}".format(s1.marks))
print("\tStudent Course={}".format(Student.crs))
print("\tStudent City={}".format(Student.city))
print("----------------------------------")
print("Second Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s2.stno))
print("\tStudent Name={}".format(s2.sname))
print("\tStudent Marks={}".format(s2.marks))
print("\tStudent Course={}".format(Student.crs))
print("\tStudent City={}".format(Student.city))
print("----------------------------------")