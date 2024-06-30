class House:
    def __init__ (self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.say_info()
    def say_info(self):
        print(f"Название: '{self.name}', количество этажей: {self.number_of_floors}")
    def __eq__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        isinstance(other, int)
        isinstance(other, House)
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        isinstance(value, int)
        isinstance(value, House)
        self.number_of_floors = self.number_of_floors + value
        self.say_info()
        return self
    def __radd__(self, value):
        isinstance(value, int)
        isinstance(value, House)
        self.number_of_floors = self.number_of_floors + value
        self.say_info()
        return self
    def  __iadd__(self, value):
        isinstance(value, int)
        isinstance(value, House)
        self.number_of_floors = self.number_of_floors + value
        self.say_info()
        return self
    def __str__(self):
        return f"{self.name}"

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1 == h2)
h1 += 10 # __iadd__
h2 = 10 + h2 # __radd__
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
