# Zадача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("введите трехзначное число: "))
import math
a = number%10
b = math.floor((number/10)%10)
c = math.floor(number/100)
sum = a + b + c

print(f"сумма трехзначного числа {number} равна {sum}")