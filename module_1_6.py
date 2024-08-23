# Практическое задание по уроку "Словари и множества."

my_dict  = {"Marat": 55, "Roma": 40, "Tanya": 23}
print(my_dict)
print(my_dict["Tanya"])
print(my_dict.get("Sasha", "Такого ключа нет!"))
my_dict.update({"Lena": 30, "Sasha": 18})
del my_dict["Roma"]
print(my_dict)

my_set = {1, 2, 3, "f", 2, 3, 4}
print(my_set)
my_set.update({5, 6})
my_set.discard(3)
print(my_set)

