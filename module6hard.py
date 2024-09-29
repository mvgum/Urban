# Дополнительное практическое задание по модулю "Множественное наследование"
import math


class Figure:
    sides_count = 0
    filled = True

    def __init__(self, color, *sides):
        self.__sides = []
        if len(sides) == 1:
            for _ in range(self.sides_count):
                self.__sides.append(sides[0])
        elif len(sides) != self.sides_count:
            for side in sides:
                self.__sides.append(1)
        else:
            for side in sides:
                self.__sides.append(side)
        self.__color = color


    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        flag = True
        for side in sides:
            if side > 0 and isinstance(side, int):
                continue
            else:
                flag = False
                break
        return flag

    def get_sides(self):
        return self.__sides

    def __len__(self,):
        perimeter = 0
        if isinstance( self.__sides, int):
            perimeter = self.__sides
        else:
            for side in self.__sides:
                perimeter += side
        return perimeter

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            sides = []
            for side in new_sides:
                sides.append(side)
            self.__sides = sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = int(sides) / (2 * 3.14)

    def get_square(self):
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self,  color, sides):
        super().__init__(color, sides)

    def get_square(self):
        p = self.__len__() / 2
        result = p
        for side in self.__sides:
            result *= (p - side)
        result = math.sqrt(result)
        return result


class Cube(Figure):
    sides_count = 12

    def __init__(self,  color, sides):
        super().__init__(color, sides)
        self.__sides = []
        for _ in range(self.sides_count):
            self.__sides.append(sides)

    def get_volume(self):
        result = self.__sides[0]
        result *= self.__sides[0]
        result *= self.__sides[0]
        return result


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
