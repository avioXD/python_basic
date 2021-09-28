

class A1:
    def __init__(self):
        print("Base class called A1")

class A2(A1):
    def __init__(self):
        print("Derived class called A2")
        super().__init__()


c = A2()



class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

      def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(f"Graduation year : {x.graduationyear}  Name {x.firstname}")


''''
Example of multilevel inheritance : 
'''

class Person:
      def __init__(self,name , age , address) :
          self.name = name 
          self.age =  age
          self.address = address

class Worker(Person): 
       def __init__(self, name, age, address, salary):
           super().__init__(name, age, address)
           self.salary = salary

class Job(Worker):
      def __init__(self, name, age, address, salary, position):
          super().__init__(name, age, address, salary)
          self.position = position
    
      def get_info(self):
          print(f'''
          Hello , {self.name} 
            Thnak you for giving your details : 
            Name: {self.name}
            age: {self.age}
            address: {self.address}

            We have decided to giyou salary of : {self.salary}
            And Job role is : {self.position}
          ''')



job = Job("Abhishek Das", 22, "Gobardanga , Kolkata , North 24 Parganas"
, 48000 , "Senior Developer")

job.get_info()



''''
Example of multiple inheritance : 
Python supports multiple inheritance

** We can only multiple inherit those classes
 which are already inheriting a same class

'''

class Car:
    def __init__(self, car_name):
        self.car_name  = car_name


class Wheel(Car): 
    def __init__(self, no_of_wheel, wheel_type, **kw):
        self.no_of_wheel = no_of_wheel
        self.wheel_type = wheel_type
        super().__init__(**kw)


class Engine(Car):
    def __init__(self, engine_cc, rpm , **kw) :
        self.engine_cc = engine_cc
        self.rpm = rpm
        super().__init__(**kw)
        
class MyCar(Engine,Wheel):
    def __init__(self, engine_cc, rpm, car_name, no_of_wheel, wheel_type):
        super(MyCar , self).__init__(engine_cc = engine_cc , rpm = rpm , car_name = car_name , no_of_wheel = no_of_wheel , wheel_type = wheel_type)
    
    def get_info(self):
        print(f"The car {self.car_name} has {self.engine_cc}cc engine with {self.rpm}rpm and {self.no_of_wheel} wheels , wheel_type of {self.wheel_type}" )


car = MyCar(250, 1800, "Dominar", 2,  "Alloy")
car.get_info()