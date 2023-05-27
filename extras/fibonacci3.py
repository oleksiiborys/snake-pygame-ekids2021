print('Поиск чисел Фибоначчи')
fib = []
fib.append(0)
print(len(fib),fib[len(fib)-1])
fib.append(1)
print(len(fib),fib[len(fib)-1])
top = 10
#for x in range(1,top+1):
while len(fib) < top:
    fib.append(fib[len(fib)-1]+fib[len(fib)-2])
    print(len(fib),fib[len(fib)-1])
print(fib)
