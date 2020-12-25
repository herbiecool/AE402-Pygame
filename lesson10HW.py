class Animal:
    def __init__(self,color, types, HP):
        self.color = color
        self.types = types
        self.HP = HP

    def hunt(self):
        self.HP = self.HP - 5
        return self.HP

    def eat(self):
        self.HP = self.HP + 5
        return self.HP

class Dog(Animal):                    
    def __init__(self,color, types, HP):
        super().__init__(color, types, HP)

    def barking(self):
        print('汪汪汪')

class BullDog(Dog):
    def __init__(self,color, types, HP):
        super().__init__(color, types, HP)                                

    def barking(self):
        print('吼吼吼')    

print('type:',int(2))
print('HP:',int(100))

color = input('color? (yellow or white)')

a = Animal(color, 2, 100)
'''
b = Dog(Animal)(color, 2, 100)
c = BullDog(Dog)(color, 2, 100)
'''
if color=='yellow':
    print(c.barking())
else:
    print(b.barking())

s = input('狀況?,hunt,or,eat')

if s=='hunt':
    print('HP',a.hunt())
else:
    print('HP',a.eat())











