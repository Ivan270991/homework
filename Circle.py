from math import pi

class Circle:
    def __init__(self):
        self.square=0

    def area(self,r):
        self.square=pi*r*r

square = Circle()
square.area(1)
print(square.square)