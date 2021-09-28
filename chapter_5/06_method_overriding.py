class Parent():
    def __init__(self):
        self.value= "Inside Parent"
    
    def show(self):
        print(self.value)

class Child(Parent):
      def __init__(self) :
          super().__init__()
          self.value = "Inside child"
      
      def show(self):
          print("Now it is ", self.value)


P = Parent()
C = Child()

P.show()
C.show()