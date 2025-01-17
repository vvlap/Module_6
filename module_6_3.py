class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print("Здесь слишком глубоко, я не могу нырнуть :(")
        else:
            self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Извини, я настроен миролюбиво :)")
        else:
            print("Будь осторожен, я атакую тебя 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    """Птицы"""
    beak = True
    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1,4)} eggs for you')

class AquaticAnimal(Animal):
    """Плавающие животные"""
    _DEGREE_OF_DANGER = 3
    def  dive_in(self, dz):
        self._cords[2] -= dz * int(self.speed/2)        # непонятное вычисление, подогнала под ответ, спросить не у кого

class PoisonousAnimal(Animal):
    """Ядовитые животные"""
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"


import random
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
