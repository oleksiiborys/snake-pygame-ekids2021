data2 = [1, 7, 2, 3, 4, 5, 4, 3, 2, 7, 1]

data3 = [1,3,5,7,2,4,6,8]
data4 = [1,5,3,4]

def bubble_sort(input):
    output = input.copy()
    length = len(input)
    for e in range(0, length):
        for i in range(1, length-e):
            v1 = output[i-1]
            v2 = output[i]
            if v1 > v2:
                output[i]= v1
                output[i-1] = v2
    return output

print(data2)
print(bubble_sort(data2))