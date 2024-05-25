my_dict= {"Andrey": 2005, "Alena": 1986, "Sanya": 1990 }
print("Dict: ", my_dict)
print("Existing value: ",my_dict["Andrey"])
print("No existing value: ",my_dict.get("Sveta"))
a= my_dict.pop("Alena")
print("Deleted value: ", a)
print("Modified dictionary:", my_dict)

my_set= {1, 2, "Слово", 2.5, 2, 3, 5, 5, 1, 2.5}
print("Set: ", my_set)
my_set.update({8, "Вилка"})
my_set= set(my_set)
print(my_set.discard("Слово"))
print("Modified set: ", my_set)