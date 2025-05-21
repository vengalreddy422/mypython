#Program for Storing Student Number,Name and Marks by using Classes and Objects
#InstanceDataMemberEx2.py
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
s1.sno=100
s1.name="Rossum"
s1.marks=45.67
#Place OR Store  Student Number,Name and Marks in s2 object--Instance Data members through an object
s2.stno=200
s2.sname="Travis"
s2.marks=55.55
s2.colname="JNTU"
print("------------------------------------")
print("Content of s1 object=",s1.__dict__)
print("Number of Values in s1 object=",len(s1.__dict__))
print("ID of s1 object=",id(s1))
print("------------------------------------")
print("Content of s2 object=",s2.__dict__)
print("Number of Values in s2 object=",len(s2.__dict__))
print("ID of s2 object=",id(s2))
print("------------------------------------")