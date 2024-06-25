class House:
    def __init__ (self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to (self, new_floor):
        a = 1
        if new_floor >= 1:
            while a <= new_floor:
                if new_floor > self.number_of_floors or new_floor < 1:
                    print (f"В доме '{self.name}' такого этажа не существует")
                    return
                else:
                    print (f"Дом '{self.name}', этаж номер {a}")
                    a += 1
        else:
            print (f"В доме '{self.name}' такого этажа не существует")
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
