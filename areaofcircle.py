"""2. Area of Circle by OOPS
python"""
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area:", c.area())
