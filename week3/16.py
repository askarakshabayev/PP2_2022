class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    # def show(self):
    #     return f'{self.name} - {self.surname}'

    def __str__(self):
        return f'{self.surname}'


a = Person('Askar', 'Akshabayev')
b = Person('aaa', 'bbb')

print(a)
print(b)
