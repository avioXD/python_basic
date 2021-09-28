class StaticClass:
    def __init__(self) : #constructor 
        print("Init called")

    @staticmethod
    def greet(): 
        print("Goood morning ")


StaticClass().greet()