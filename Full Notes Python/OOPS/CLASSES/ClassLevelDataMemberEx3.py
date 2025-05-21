#Program for Demonstrating the need of Class Level Data Members
#ClassLevelDataMemberEx3.py
class Employee:pass

#Main Program
#Define Class Level Data Members in Main Program
Employee.compname="IBM"
Employee.city="HYD"  # Here compname and city are called Class Level Data Memebrs
#Here are accessing the Class Level Data Members by using Class Name
print("Employee Comp Name=",Employee.compname)
print("Employee Comp City=",Employee.city)

