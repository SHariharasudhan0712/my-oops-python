"""1. OOPS Demo Code
python"""
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

al = A("Alice", 25)
al.greet()
