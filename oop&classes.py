'''class Bike:
 name=" "
 gear=0
 engine=00 
bike1=Bike()
bike1.gear=4
bike1.name="superstar bike"
bike1.engine=70
print(f"Name: {bike1.name}, Gears:{bike1.gear},engine:{bike1.engine}")'''


'''class Human:
 attr1="human"
 attr2="student"

 def fun(self):
  print("I'm a",self.attr1)
  print("I'm a",self.attr2)

Rodger=Human()

print(Rodger.attr1)
Rodger.fun() '''



'''# Sample class with init method
class Person:
	# init method or constructor
	def __init__(self, name):
		self.name = name
	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)
p = Person('pasha')
p.say_hi()'''



'''# define a class
class Employee:
    # define an attribute
    employee_id = 0
# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()
# access attributes using employee1
employee1.employeeID = 199
print(f"Employee ID: {employee1.employeeID}")
# access attributes using employee2
employee2.employeeID = 200
print(f"Employee ID: {employee2.employeeID}")'''


       
'''class Room:
 length=0.0
 breadth=0.0

def calculate_area(self):
   print("area of room=",self.length * self.breath)
study_room=Room()
study_room.length=30
study_room.breadth=20
study_room.calculate_area()'''


class Employee:
    __id=0
    __name=""
    __gender=""
    __city=""
    __salary=0
    def setData(self):
        self.__id=int(input("Enter Id:\t"))
        self.__name = input("Enter Name:\t")
        self.__gender = input("Enter Gender:\t")
        self.__city = input("Enter City:\t")
        self.__salary = int(input("Enter Salary:\t"))
    def showData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)


def main():
    #Employee Object
    emp=Employee()
    emp.setData()
    emp.showData()

if __name__=="__main__":
    main()