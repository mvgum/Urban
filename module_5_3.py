# Домашняя работа по уроку "Перегрузка операторов."

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors == other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __lt__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors < other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __le__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors <= other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __gt__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors > other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __ge__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors >= other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __ne__(self, other):
        if isinstance(other, House):
            if isinstance(other.number_of_floors, int):
                return self.number_of_floors != other.number_of_floors
            else:
                print(f'"Объект {other.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")

    def __add__(self, value):
        if isinstance(self, House):
            if isinstance(self.number_of_floors, int):
                self.number_of_floors += value
            else:
                print(f'"Объект {self.number_of_floors} не является целым числом!"')
        else:
            print("Второй объект не является элементом класса House!")
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

