# Method is a fucntion that is inside the class
# You have to use the self parameter that is being passed onto the method
import random

class Employee:
    nature = "lazy or hardworking, nothing in the middle"

    def __init__(self, name, resilience, lazy):
        self.name = name
        self.resilience = resilience
        self.lazy = lazy

    def afternoon(self):
        print(f"{self.name} wants to go home but will stay as she has got a strong {self.resilience}")  
        print(f"{self.name} will not stay as she is {self.lazy}")

Employee1 = Employee("Sophie", "work ethic", "not lazy")    
Employee2 = Employee("Tasha", "work ethic", "lazy")  

Employee1.afternoon()
Employee2.afternoon()

class Square:
    width = 4
    height = 4

    def area(self):
        return self.height * self.width
    
my_shape = Square()    
print(my_shape.area())
            




