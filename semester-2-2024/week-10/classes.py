class Superhero:
    def __init__(self, name, power, age):
        self.name = name
        self.power = power
        self.age = age

    def birthday(self):
        self.age += 1
        return self.age

    def __str__(self):
        return f'{self.name} has the power to {self.power} and is {self.age} years old.'


batman = Superhero('Batman', 'Money', 30)
print(batman.name)
print(batman.birthday())
print(batman.birthday())
print(batman)
