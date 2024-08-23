# Задание "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
rating = {}
students = list(students)
students = sorted(students)
if len(students) == len(grades):
    for i in range(len(grades)):
        rating[students[i]] = sum(grades[i]) / len(grades[i])
else:
    print("Облом")
print(rating)