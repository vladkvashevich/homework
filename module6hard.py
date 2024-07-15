import math
class Figure:
    sides_count = 0

    def __init__(self, sides, color):
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = sides
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def _is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def _is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__([radius], color)
        self.radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)
    def set_sides(self, radius):
        if self._is_valid_sides(radius):
            self._Figure__sides = [radius]
            self.__radius = radius

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        super().__init__()

    def get_square (self, a, b, c):
        a, b, c = self.get_sides()
        p = (a + b + c)/2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_lenght):
        super().__init__([side_lenght] * self.sides_count, color)

    def get_volume(self):
        side = self.get_sides()[0]
        return side ** 3

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._Figure__sides = list(new_sides)

    def get_sides(self):
        return self._Figure__sides


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