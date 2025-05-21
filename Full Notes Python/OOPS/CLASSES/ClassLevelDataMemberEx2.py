#Program for Demonstrating the need of Class Level Data Members
#ClassLevelDataMemberEx2.py
class Employee:
    compname="IBM"
    city="HYD" # Here compname,city are called Class Level Data Members

#Main Program
#Here are accessing the Class Level Data Members by using Objects of Employee
eo1=Employee() # Object Created
print("Employee Comp Name=",eo1.compname)
print("Employee Comp City=",eo1.city)
print("---------------------------")
#Here are accessing the Class Level Data Members by using Objects of Employee
eo2=Employee() # Object Created
print("Employee Comp Name=",eo1.compname)
print("Employee Comp City=",eo1.city)
print("---------------------------")



