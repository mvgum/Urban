# Задание "Слишком древний шифр"

def divider(num):
    not_primes = []
    for n in range(3, num):
        if (num % n) == 0:
            not_primes.append(n)
    return not_primes


def couple(num):
    list_ = []
    for i in range(1, num // 2 + 1):
        list_.append((i, num - i))
        if num - i == i or num - i == i or num - i - 1 == i + 1:
            break
    return list_


number = 20
choice = []
for n in divider(number):
    choice += couple(n)

couple_num = couple(number)

result = []
count = 0
while count != number // 2:
    count += 1
    for n in choice:
        if n[0] == count:
            result.append(n)
    for m in couple_num:
        if m[0] == count:
            result.append(m)
print(result)
