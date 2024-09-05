# Самостоятельная работа по уроку "Модули и пакеты".

from fake_math import divide as div_zero
from true_math import divide as div_inf


result1 = div_zero(69, 3)
result2 = div_zero(3, 0)
result3 = div_inf(49, 7)
result4 = div_inf(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
