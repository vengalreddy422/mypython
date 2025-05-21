#Program for Demonstrating generator
#GenEx5.py
def  getcourses():
	yield "PYTHON"
	yield "HTML"
	yield "Django"
	yield  "MongoDB"
#Main Program
cg=getcourses()
print(next(cg))
print(next(cg))
print(next(cg))
print(next(cg))
