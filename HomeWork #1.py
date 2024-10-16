# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Зачем нужно наследование"

class Animal:
    alive = True  # живой
    fed = False  # накормленный

    def __init__(self, name):
        self.name = name


class Mammal(Animal):

    def eat(self, food):
        #food.name = food <---- ВОТ ИЗ-ЗА ЭТОЙ СТРОЧКИ НЕ РАБОТАЛ ВЫВОД
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.alive = True  # живой
            self.fed = True  # накормленный
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # живой
            self.fed = False  # накормленный


class Predator(Animal):
    def eat(self, food):
        #food.name = food <---- ВОТ ИЗ-ЗА ЭТОЙ СТРОЧКИ НЕ РАБОТАЛ ВЫВОД
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.alive = True  # живой
            self.fed = True  # накормленный
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False  # живой
            self.fed = False  # накормленный


class Plant:

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
