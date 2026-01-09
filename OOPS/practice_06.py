class Shape:
    def area(self): pass
class Square(Shape):
    def __init__(self,s): self.s=s
    def area(self): return self.s*self.s
print(Square(4).area())