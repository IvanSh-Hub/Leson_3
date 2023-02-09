# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]

def mult(listArg):
    resultList =[]
    check = len(listArg)%2 == 0
    length = 0
    if check:
        length = int(len(listArg)/2)
    else:
        length = int(len(listArg)/2 + 1)

    print(length)
    for i in range(length):
        resultList.append(listArg[i] * listArg[len(listArg)-i-1])
    return resultList

print(mult(list))
