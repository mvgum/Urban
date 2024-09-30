# Домашнее задание по теме "Режимы открытия файлов"


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f"{self.name}, {self.weight}, {self.category}")


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, "r")
        result = file.read()
        file.close()
        return result

    def add(self, *products):
        for prod in products:
            prod = prod.__str__()
            catalog = self.get_products()
            if prod in catalog:
                print(f'Продукт {prod} уже есть в магазине')
            else:
                file = open(self.__file_name, "a")
                file.write(prod + "\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
