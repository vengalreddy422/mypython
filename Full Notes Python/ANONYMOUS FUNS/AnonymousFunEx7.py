#Accept the Value and Display Its Nature
#AnonymousFunEx7.py

gettypevalue=lambda val:"Digit" if val.isdigit() else "Alphabet" if val.isalpha() \
    else "Alpha-numeric" if val.isalnum() else "'   ' Space" if val.isspace() else "Special Symbol" \
    if ((not val.isdigit()) and (not val.isalpha())
        and( not val.isspace()) and (not val.__contains__("."))) and  (not val.__contains__("@")) else "Other Value"


#main Program
v=input("Enter Any Value:")
typeval=gettypevalue(v)
print("{} is {}".format(v,typeval))