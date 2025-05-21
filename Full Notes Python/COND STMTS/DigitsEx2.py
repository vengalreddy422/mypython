#Program for Accepting the Digit and Display Its name
#DigitsEx2.py
d={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
dig=int(input("Enter the Digit:"))
print("{} is {}".format(dig,d.get(dig) if d.get(dig)!=None else "+VE Number" if dig>9 else "-VE Number" if dig<0 and dig not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-VE Digit"))
