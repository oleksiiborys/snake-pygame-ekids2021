# Перевірка чи фраза є паліндромом(читається спереду назад і навпаки однаково)

# а роза упала на лапу азора

data1 = ["a", "q", "b", "c", "d", "b", "w", "a"]
data2 = [1, 7, 2, 3, 4, 5, 4, 3, 2, 7, 1]
data3 = [1, 2, 3]
data4 = [5, 6, 7]
data5 = [1, 2, 3, 1, 2, 3]


def check_palindrome(input):
    # print(input)
    # print(len(input))
    # print(range(0,len(input)))
    counter = 0
    for i in range(0, round(len(input))):
        print(str(input[i]) + " - " + str(input[len(input) - i - 1]))
        counter += 1
        if (input[i] != input[len(input) - i - 1]):
            return False

    print("Iterations - " + str(counter))
    return True

print(str(data1) + " - " + str(check_palindrome(data1)))
print(str(data2) + " - " + str(check_palindrome(data2)))

