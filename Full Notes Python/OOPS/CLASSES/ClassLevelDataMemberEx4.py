#Program for Demonstrating the need of Class Level Data Members
#ClassLevelDataMemberEx4.py
class Employee:pass

#Main Program
#Define Class Level Data Members in Main Program
Employee.compname="IBM"
Employee.city="HYD"  # Here compname and city are called Class Level Data Memebrs
#Here are accessing the Class Level Data Members by using Object Name
eo1=Employee()
print("content of eo1=",eo1.__dict__)
print("Employee Comp Name=",eo1.compname)
print("Employee Comp City=",eo1.city)

