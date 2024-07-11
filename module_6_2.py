class Vehicle:
    def __init__ (self,owner, __model, __color, __engine_power ):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self, __model):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return print(f"Цвет: {self.__color}")

    def print_info(self):
        print(f"Модель: {self.__model}\nМощность двигателя: {self.__engine_power}\nЦвет: {self.__color}\nВладелец: {self.owner} ")

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = new_color
        else:
            print(f"Невозможно покрасить в {self.new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


