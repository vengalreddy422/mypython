#VoterEx2.py
while(True):
    age=int(input("Enter Ur Age:"))
    if(age>=18):
        break
    else:
        print("\t{} Years Citizen is not eligible to vote:".format(age))
print("{} Years Citizen is Eligible to Vote:".format(age))