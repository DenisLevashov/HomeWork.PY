# Задача 6: Счастливый шестизначный билет

# 385916 -> yes
# 123456 -> no

namber = int(input("Введите номер билета: "))
import math
a1 = math.floor(namber/1000%10)
a2 = math.floor(namber/10000%10)
a3 = math.floor(namber/100000)
b1 = math.floor(namber%10)
b2 = math.floor(namber/10%10)
b3 = math.floor(namber/100%10)
if (a1 + a2 + a3) == (b1 + b2 + b3):
    print("билет счастливый")
else :
    print("билет не счастливый")