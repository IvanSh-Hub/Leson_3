
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def conversionToBin(number):
    return bin(number)

print(conversionToBin(3)[2:])
