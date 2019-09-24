class Person:
    def __init__(self, n, s, q=1):
        self.name = n
        self.surname = s
        self.qualification = q
        print('yes') 

    def inf(self):
        return 'name:   surname: {} qualification: {}'.format(self.name,
                self.surname, self.qualification)

person = Person('Ivan', 'Glyatsevich')
print(person.inf())