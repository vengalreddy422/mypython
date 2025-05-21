#program for Generating Mul Table by using Classes and Object with Instance Methods
#InstanceMethodEx7.py
class MulTable:
    def getN(self):
        self.n=int(input("Enter a Number for Generating Mul table:"))
    def table(self):
        if(self.n<=0):
            print("{} is Invalid Input".format(self.n))
        else:
            print("------------------------------------")
            print("Mu table for :{}".format(self.n))
            print("------------------------------------")
            for i in range(1,11):
                print("\t{}x{}={}".format(self.n,i,self.n*i))
            print("------------------------------------")

#Main Program
mt=MulTable() # Object Creation
mt.getN()
mt.table()
