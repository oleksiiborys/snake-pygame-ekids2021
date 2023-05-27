data2 = [1, 7, 2, 3, 4, 5, 4, 3, 2, 7, 1]
data3 = [1, 3, 5, 7, 2, 4, 6, 8]
data4 = [1, 5, 3, 4]

def sort(input, descending = False):
    result = input.copy()
    length = len(result)
    for i1 in range(0, length):
        for i2 in range(1, length - i1):
            el1 = result[i2]
            el2 = result[i2-1]
            if ((el2 > el1 and not descending) or
                    (el2 < el1 and descending)):
                result[i2] = el2
                result[i2-1] = el1

    return result


print(sort(data2))
print(sort(data2, descending=True))
print(sort(data3))
print(sort(data3, descending=True))
print(sort(data4))
print(sort(data4, descending=True))