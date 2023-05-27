def fib(n):
    if n == 0:
        return 0
    if n==1 or n==2:
        return 1
    fib_num = fib(n-1) + fib(n-2)
    return fib_num


res = []

for i in range(0,10):
    res.append(fib(i))

print(res)

