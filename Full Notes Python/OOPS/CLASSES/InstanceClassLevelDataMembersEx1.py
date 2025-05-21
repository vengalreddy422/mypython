#Program for Storing Student Number,Name and Marks and Course
# for all Students  by using Classes and Objects
#InstanceClassLevelDataMembersEx1.py
class Student:
    crs="PYTHON" # Here crs is called Class Level Data Member

#main Program
s1=Student() # Creating an Object of Student Class
s2=Student() # Creating an Object of Student Class
#Place OR Store  Student Number,Name and Marks in s1 object--Instance Data members through an object
s1.sno=100
s1.name="Rossum"
s1.marks=45.67
#Place OR Store  Student Number,Name and Marks in s2 object--Instance Data members through an object
s2.stno=200
s2.sname="Travis"
s2.marks=55.55
#Dsiplay the Object s1 Data
print("----------------------------------")
print(s1.__dict__)
print("First Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s1.sno))
print("\tStudent Name={}".format(s1.name))
print("\tStudent Marks={}".format(s1.marks))
print("\tStudent Course={}".format(Student.crs))
print("----------------------------------")
print(s2.__dict__)
print("Second Student Data")
print("----------------------------------")
print("\tStudent Number={}".format(s2.stno))
print("\tStudent Name={}".format(s2.sname))
print("\tStudent Marks={}".format(s2.marks))
print("\tStudent Course={}".format(Student.crs))
print("----------------------------------")