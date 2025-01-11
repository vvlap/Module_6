class Animal:
    alive = True            #живой
    fed = False             #накормленный
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            self.fed = True
            print(f'{self.name} съел {food.name} и насытился')
        else:
            self.alive = False
            print(f'{self.name} съел {food.name} и погиб')

class Plant:
    edible = False          #съедобность
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    """Млекопитающие"""

class Predator(Animal):
    """Хищники"""

class Flower(Plant):
    """Цветы"""

class Fruit(Plant):
    """Фрукты"""
    edible = True


a1 = Predator('Волк')
a2 = Mammal('Заяц')
p1 = Flower('Борщевик')
p2 = Fruit('Яблоко')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)