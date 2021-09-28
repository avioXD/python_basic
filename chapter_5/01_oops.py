'''
'self' represents the instance of the class.
By using the “self” keyword we can access the attributes and methods
of the class in python. It binds the attributes with the given arguments.
The reason you need to use self.
is because Python does not use the @ syntax to refer to instance attributes.
'''

class Number:
    def sum(self, a , b ) :
        return   a + b
    def f(self):
        return "Hello World"



num = Number()
print(num.f())
print(num.sum( 5 , 6))
 

'''
The instantiation operation (“calling” a class object) creates an empty object. 
Many classes like to create objects with instances customized to a specific initial state.
Therefore a class may define a special method named __init__(), like this:
'''

class Complex: 
    def __init__(self, realpart, subpart):
        self.r = realpart
        self.i = subpart

x = Complex(3.0, -4.5)
print(x.r ," ", x.i)



class Car:
    def __init__(self, name) :
        self.name = name
        self.cars = []

    def add_car(self, new_car):
        self.cars.append(new_car)
    



car = Car("Marcidies")
car.add_car("Sizuku")
car.add_car("Range Rover")
car.add_car("Kiya")
car.add_car("Tata")

print(car.cars)


