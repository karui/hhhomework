class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __repr__(self):
        return f'{self.brand} {self.model}'

class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    carList = []
    nextCarIndex = None

    def __init__(self, *cars):
        self.carList.extend(cars)

    def __iter__(self):
        # return iter(self.carList)
        return self

    def __next__(self):
        self.nextCarIndex = 0 if self.nextCarIndex is None else self.nextCarIndex + 1
        try:
            return self.carList[self.nextCarIndex]
        except IndexError:
            self.nextCarIndex = None
            raise StopIteration

    def __repr__(self):
        return '\n'.join([ f'{i:>2}. {car}' for i, car in enumerate(self.carList)])

    def __len__(self):
        return len(self.carList)

    def __getitem__(self, i):
        return self.carList[i]

    def add(self, car):
        self.carList.append(car)

    def delete(self, carIndex):
        self.carList.pop(carIndex)


car1 = Car('Haval', 'H6')
car2 = Car('Chery', 'Tiggo 5')
car3 = Car('Lifan', 'X60')
car4 = Car('Dongfeng', 'AX7')
car5 = Car('FAW', 'Besturn X80')

garage = Garage(car1, car2)
garage.add(car3)
garage.add(car4)
garage.add(car5)
garage.delete(0)

print(garage)

print()

for car in garage:
    print(car)
