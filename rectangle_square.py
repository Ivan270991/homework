class Rectangle:
    def __init__(self):
        self.perimetr=0

    def calculate_perimetr(self,a,b):
        self.perimetr=(a+b)*2


class Square:
    def __init__(self):
        self.perimetr=0

    def calculate_perimetr(self,a):
        self.perimetr=a*4


rec=Rectangle()
rec.calculate_perimetr(2,3)
print(rec.perimetr)
sq=Square()
sq.calculate_perimetr(1)
print(sq.perimetr)