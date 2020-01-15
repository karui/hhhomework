from random import randint

# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def gen(N):
    for i in range(N):
        yield randint(1, 99)

# написать генераторное выражение, которое делает то же самое
N = 11
genexp = (randint(1,99) for i in range(N))

print([number for number in gen(11)])
print([number for number in genexp])
