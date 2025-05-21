#PolyEx25.py
class India:
    def lang(self):
        print("Indians Speaks Multiple Languages")
    def cnttype(self):
        print("India is a Developing Country")
class USA:
    def lang(self):
        print("Americans Speaks English Language")
    def cnttype(self):
        print("USA is a Developed Country")
#Main Program
#io=India()
#us=USA()
for obj in (India(),USA()):
    obj.lang()
    obj.cnttype()
    print("-----------------------------------")
# Here obj contains Ref of India() and USA()
# and hence obj is called Polymorphic Object


