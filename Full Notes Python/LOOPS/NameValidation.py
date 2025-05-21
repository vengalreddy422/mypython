#Namevalidation.py
while(True):
    sname=input("Enter UR name:") # GUIDO VAN ROS2UM
    words=sname.split() # [GUIDO, VAN ,ROS2UM]
    if(len(words)==0):
        print("Name should not empty--try again")
    else:
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(not res):
            print("\t{} is Invalid Name-try again".format(sname))
        else:
            break


print("UR Name is valid=",sname)




