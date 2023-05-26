# В списку даних знайти перше унікальне значення

data1 = ["a", "q", "b", "c", "d", "b", "w", "a"]
data2 = [1, 7, 2, 3, 4, 5, 4, 3, 2, 7, 1]
data3 = [1, 2, 3]
data4 = [5, 6, 7]
data5 = [1, 2, 3, 1, 2, 3]

def check_unique(input):
    for i in range(0, len(input)):
        element = input[i]
        input_copy = input.copy()
        input_copy.pop(i)
        if element not in input_copy:
            return element

    return ""

print(check_unique(data1) == "q")
print(check_unique(data2) == 5)
print(check_unique(data3) == 1)

