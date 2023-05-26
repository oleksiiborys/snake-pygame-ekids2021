# Перевірка чи фраза є паліндромом(читається спереду назад і навпаки однаково)

# а роза упала на лапу азора

data1 = ["a", "q", "b", "c", "d", "b", "w", "a"]
data2 = [1, 2, 3, 4, 5, 4, 3, 2, 1]


num = "123"
print(list(num))
rev = reversed(num)
print(list(rev))


def check_palindrome(input):
    return input == list(reversed(input))

# def check_palindrome(input):
#     print(input[0: round(len(input)/2)])
#     print(input[round(len(input)/2): len(input)])
#     print(''.join(input))
#
#     return input == list(reversed(input))


print(str(data1) + " - " + str(check_palindrome(data1)))
print(str(data2) + " - " + str(check_palindrome(data2)))
