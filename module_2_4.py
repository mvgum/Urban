# Домашняя работа по уроку "Цикл for. Элементы списка."

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for num in numbers:
    if num == 1:
        continue
    primes.append(num)
    for n in range(2, num):
        if (num % n) == 0:
            not_primes.append(primes.pop())
            break
print(primes)
print(not_primes)
