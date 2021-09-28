
'''
We can't create multiple constructor in Python
'''

class Employee1:
    salary = 40000
    def __init__(self, name, address, age, salary):
        self.name =  name
        self.address = address
        self.age = age
        self.salary = salary
        
    def get_sal(self):
        return  self.salary

    def get_info(self):
        print(f"Employee  {self.name} from {self.address} get salary of {self.get_sal()} at age {self.age}")


# emp1 = Employee("Abhishek ", "Gobardanga", 23) #this is not possible
emp2 = Employee1("Abhishek", "Gobardanga", 23, 560000)
# print(emp1.get_sal())
emp2.get_info()


# multiple constructor :

class Employee2:
    salary = 40000
    def __init__(self, *args):
        if len(args) == 4 :
            self.name =  args[0]
            self.address = args[1]
            self.age = args[2]
            self.salary = args[3]
        elif len(args) == 3:
             self.name =  args[0]
             self.address = args[1]
             self.age =args[2]

    def get_name(self):
        return self.name

    def get_sal(self):
        return  self.salary

    def get_info(self):
        print(f"Employee  {self.name} from {self.address} get salary of {self.get_sal()} at age {self.age}")


emp1 = Employee2("Abhishek ", "Gobardanga", 23)
emp2 = Employee2("Abhishek", "Gobardanga", 23, 560000)
emp1.get_info()
emp2.get_info()

class Name:
    def __init__(self,name) :
        self.name = name
        print(f"So Employee functions returns this name: {self.name} ")

nameFun = Name(emp1.get_name())



'''
Another way to achive multiple constructor: 
By using dispatch
'''
from multipledispatch import dispatch

class Employee3:
     salary = 30000
     
     @dispatch(str , str , int , int )
     def __init__(self, name, address, age , salary = 40000):
        self.name =  name
        self.address = address
        self.age = age
        self.salary = salary

     @dispatch(str , str , int)
     def __init__(self, name, address, age ):
        self.name =  name
        self.address = address
        self.age = age

     def get_name(self):
        return self.name

     def get_sal(self):
        return  self.salary

     def get_info(self):
        print(f"Employee  {self.name} from {self.address} get salary of {self.get_sal()} at age {self.age}")


emp1 = Employee3("Abhishek ", "Gobardanga", 23)
emp2 = Employee3("Abhishek", "Gobardanga", 20 , 560000)
emp1.get_info()
emp2.get_info()