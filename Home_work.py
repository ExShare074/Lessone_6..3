#1. Создаем базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и
# методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуем наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавляем специфические атрибуты и переопределяем методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируем полиморфизм: создаем функцию `animal_sound(animals)`, которая принимает список животных и вызывает
# метод `make_sound()` для каждого животного.

#4. Используем композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создаем классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("чирик-чирик")

    def eat(self):
        print("Семена и насекомые")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    def make_sound(self):
        print("рррррр")
    def eat(self):
        print("Молоко и мясо")

class Reptile(Animal):
    def __init__(self, name, age, sound):
        super().__init__(name, age)
        self.sound = sound
    def make_sound(self):
        print("щщщщщщщ")
    def eat(self):
        print("Животные")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def add_employee(self, employee):
        self.employees.append(employee)

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Feeding {animal.name}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Healing {animal.name}")

#Пример использования:
bird1 = Bird("Tweety", 2)
mammal1 = Mammal("Koala", 5)
reptile1 = Reptile("Crocodile", 3, "рррррр")
zoo = Zoo()
zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

for animal in zoo.animals:
    zookeeper.feed_animal(animal)
    veterinarian.heal_animal(animal)