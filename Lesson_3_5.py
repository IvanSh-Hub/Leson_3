
def fullFibo(n):
    list1 = []
    list2 = []

    f0 = 0
    f1 = f2 = rf1 = 1
    rf2 = -1
    list1.extend([f0, f1, f2])
    list2.extend([rf1, rf2])
    for i in range(n-1):
        f1, f2 = f2, f1 + f2
        rf1, rf2 = rf2, rf1 - rf2
        list1.append(f2)
        list2.append(rf2)
    return list(reversed(list2)) + list1

n = 8
print(fullFibo(n))


