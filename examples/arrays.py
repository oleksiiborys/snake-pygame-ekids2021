print("-0-----------")

array1 = (1, 3, 5)
# array1[1] = 7 # не_змінні значення
print(array1)

print("-1-----------")

array2 = [1, 3, 5]

array2.insert(1, 2)
array2.insert(3, 4)
del array2[2]
array2.append(6)

print(array2)
array2[2] = "0"  # змінні значення
print(array2)

print("-2-----------")

alphabet = ["a", "b", "c", "d", "e"]
print(alphabet)
for letter in alphabet:
    print(letter)

print("-3-----------")
alphabet_length = alphabet.__len__()
i = alphabet_length-1
while i>=0:
    print(alphabet[i])
    i -= 1

print("-4-----------")

alphabet2 = [
    [1, "a"],
    [2, "b"],
    [3, "c"],
    [4, "d"],
    [5, "e"]
]

for pair in alphabet2:
    print(pair)
    print(pair[0].__str__() + " - " + pair[1])

print("-the-end-----")
