#Program for Demonstrating the need of Class Level Data Members
#ClassLevelDataMemberEx1.py
class Employee:
    compname="IBM"
    city="HYD" # Here compname,city are called Class Level Data Members

#Main Program
#Here are accessing the Class Level Data Members by using Class Name
print("Employee Comp Name=",Employee.compname)
print("Employee Comp City=",Employee.city)


