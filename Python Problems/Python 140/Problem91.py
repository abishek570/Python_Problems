class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self):
        super().__init__()
    def area(self,length):
        return length**2
    
shape = Shape()
square = Square()
print(shape.area())
print(square.area(50))