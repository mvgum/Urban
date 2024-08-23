# Домашняя работа по уроку "Функции в Python.Функция с параметром."

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return  matrix

temp = get_matrix(4, 2, 13)
print(temp)
