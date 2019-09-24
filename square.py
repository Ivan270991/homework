class Square:
    def __init__(self, a):
        self.side = a

    def change_size(self, b):
        self.side = self.side + b


sq=Square(6)
sq.change_size(2)
print(sq.side)