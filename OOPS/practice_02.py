class Circle:
    def __init__(self,r): self.r=r
    def area(self): return 3.14*self.r*self.r

print(Circle(5).area())