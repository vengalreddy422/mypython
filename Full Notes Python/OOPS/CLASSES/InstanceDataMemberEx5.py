#Program for Storing Student Number,Name and Marks by using Classes and Objects
#InstanceDataMemberEx5.py
class Student:pass

#main Program
s1=Student() # Creating an Object of Student Class
s2=Student() # Creating an Object of Student Class
print("------------------------------------")
print("Content of s1 object=",s1.__dict__)
print("Number of Values in s1 object=",len(s1.__dict__))
print("ID of s1 object=",id(s1))
print("------------------------------------")
print("Content of s2 object=",s2.__dict__)
print("Number of Values in s2 object=",len(s2.__dict__))
print("ID of s2 object=",id(s2))
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
s2.colname=input("Enter Second Student College Name:")
#Dsiplay the Object s1 Data
print("----------------------------------")
print("First Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s1.sno))
print("\tStudent Name={}".format(s1.name))
print("\tStudent Marks={}".format(s1.marks))
print("----------------------------------")
print("Second Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s2.stno))
print("\tStudent Name={}".format(s2.sname))
print("\tStudent Marks={}".format(s2.marks))
print("\tStudent College Name={}".format(s2.colname))
print("----------------------------------")