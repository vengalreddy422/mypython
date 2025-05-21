#DictCompEx2.py
nowds=int(input("Enter How Many Week Days:"))
wd={}
for i in range(1,nowds+1):
    wkd=input("Enter {} Week Day Name:".format(i))
    wd[i]=wkd
else:
    print(wd)

