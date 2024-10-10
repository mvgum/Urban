# Домашнее задание по теме "Декораторы".

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for num in range(2, res):
            if res % num == 0:
                print("Составное")
                break
            if num == (res - 1):
                print("Простое")
        return res
    return wrapper


@is_prime
def sum_three(first, second, third):
    summer = first + second + third
    return summer


result = sum_three(2, 3, 6)
print(result)
