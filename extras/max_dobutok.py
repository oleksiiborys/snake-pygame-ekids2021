# Знайти максимальний добуток з двох чисел з списку чисел

data2 = [1, 7, 2, 3, 4, 5, 4, 3, 2, 7, 1]
data3 = [1, 2, 3]
data4 = [5, 6, 7]
data5 = [1, 2, 3, 1, 2, 3]

def max_dobutok(input): # [1, 2, 3]
    result = 0
    for i in range(0, len(input)):
        element = input[i] # 1
        input_copy = input.copy()
        input_copy.pop(i) # [2, 3]
        for element2 in input_copy:
            temp_result = element * element2
            if temp_result > result:
                result = temp_result

    return result

print(max_dobutok(data2) == 49)
print(max_dobutok(data3) == 6)
print(max_dobutok(data4) == 42)
print(max_dobutok(data5) == 9)
