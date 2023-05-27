
def fibonacci_generator(max_count):
    arr = [0,1]

    while len(arr) < max_count:
        arr.append(arr[-1] + arr[-2])

    return arr

print(fibonacci_generator(5)) # print("[0, 1, 1, 2, 3, 5]")
print(fibonacci_generator(7))
print(fibonacci_generator(13))
print(fibonacci_generator(17))
