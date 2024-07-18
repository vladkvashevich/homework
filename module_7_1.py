from pprint import pprint
class Product:
    def __init__(self, name, weigth, category):
        self.name = name
        self.weigth = weigth
        self.category = category

    def __str__(self):
        return f" Название - {self.name}, Вес - {self.weigth}, Категория - {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, "r")
        f = file.read()
        file.close()
        return f

    def add(self, *products):
        file = open(self.__file_name, "a", encoding = "utf-8")
        current_products = self.get_products()
        for i in products:
            if i.name in current_products:
                print(f"Продукт {i.name} уже есть в магазине")
            else:
                file.write(str(i)+ "\n")
                current_products += str(i)+"\n"
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

