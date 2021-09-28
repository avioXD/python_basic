'''
A Class in Python has three types of access modifiers:

1. Public Access Modifier
2. Protected Access Modifier
3. Private Access Modifier
'''

'''
Public Access Modifier:
The members of a class that are declared public are easily 
accessible from any part of the program. 
All data members and member functions of a class are public by default. 

example: 
'''

class Greet:
    def __init__(self, name ):
           # public data members
           self.name = name
    # public member function        
    def message(self):
        print(f"Hello {self.name} ! Good morning")


greet = Greet("Abhishek")
greet.message()
print(greet.name , " Direct accessed variable") # here we can directly access the  variable name inside greet object


'''
Protected Access Modifier:
The members of a class that are declared protected are only accessible 
to a class derived from it. Data members of a class are declared 
protected by adding a single underscore ‘_’ symbol before 
the data member of that class. 

example: 
'''

class Student:
    
     # protected data members
    _name: None
    _roll: None
    _branch: None

     # constructor
    def __init__(self, name , roll , branch) :
          self._name = name
          self._roll = roll
          self._branch = branch      

    # protected member function  
    def _show_info(self):
 
          # accessing protected data members
          print("Roll: ", self._roll)
          print("Branch: ", self._branch)

class Boy(Student):
    _gender: None

    def __init__(self, name, roll, branch, gender):
        super().__init__(name, roll, branch)
        self._gender = gender
    # public member function
    def show_protected_info(self):        
         # accessing protected data members of super class
         print("Name: ", self._name)      
          
         # accessing protected member functions of super class
         self._show_info()

         print("Gender: ", self._gender) 
 

s = Boy("Abhishek ", 98 , "CSE", "Male")
s._show_info() # we can  also access protected function directly through object but in same package
s.show_protected_info()


'''
Private Access Modifier:
The members of a class that are declared private are accessible within 
the class only, private access modifier is the most secure access modifier. 
Data members of a class are declared private by adding a double 
underscore ‘__’ symbol before the data member of that class. 

Example: 
'''

class Employee:
    # private members
    __name:None
    __age: None
    __salary: None

    # constructor
    def __init__(self, name , age , sal):
        self.__name = name
        self.__age = age
        self.__salary = sal


    # private member function 
    def __show_info(self):
        # accessing private data members
        print("\n\nEmployee details")
        print("Name: ", self.__name)
        print("Age: ", self.__age)
        print("Salary: ", self.__salary)


    # public member function
    def show_private_info(self):
        # accesing private member function
        self.__show_info()


Emp = Employee("Abhishek Das", 22 , 45000)
#Emp.__show_info() # We can't do that because it's a private member function of class
Emp.show_private_info()