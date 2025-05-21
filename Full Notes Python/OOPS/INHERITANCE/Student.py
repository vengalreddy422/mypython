#Student.py<----File Name and Module Name
import College
class Student(College.College):
    def getStudDet(self):
        self.sno=int(input("Enter Student Number:"))
        self.name=input("Enter Student Name:")
        self.crs=input("Enter Student Course:")
    def dispStudDet(self):
        print("-" * 50)
        print("Student Number:{}".format(self.sno))
        print("Student Name:{}".format(self.name))
        print("Student Course:{}".format(self.crs))
        print("-" * 50)
