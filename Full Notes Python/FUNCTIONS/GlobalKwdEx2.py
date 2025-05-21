#Program for Demonstrating the need of global keyword
#GlobalKwdEx2.py
def modify1():
	global a,b
	a=a+1
	b=b+1
	
def modify2():
	global a,b
	a=a*2
	b=b*2
def modify3():
	c=a+10 # Here No Need to write global kwd bcoz we are just accessing global Var Vals
	d=b+10
	print("\tIn Modify3(): c={} d={}".format(c,d))

#Main Program
a,b=10,20 # Here 'a' and 'b'  are  called Global Variable
print("Main Program: Before modify1(): a={} b={}".format(a,b))
modify1() # Function Call
print("Main Program: after modify1(): a={} b={}".format(a,b))
modify2()
print("Main Program: after modify2(): a={} b={}".format(a,b))
modify3()
print("Main Program: after modify3(): a={} b={}".format(a,b))