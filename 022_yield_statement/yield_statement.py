# yield can be used inside functions instead of return
# this will make function behave like generator


# Squares generator sample
def generator_squares(number):
    for i in range(0, number + 1):
        yield i ** 2


generator_sq = generator_squares(10)
print('Generator squares!')
print(next(generator_sq))
print(next(generator_sq))
print(next(generator_sq))
print(next(generator_sq))
print(next(generator_sq))
print('*' * 20)


"""
Числа Фибоначчи (строка Фибоначчи) — числовая последовательность,
первые два числа которой являются 0 и 1,
а каждое последующее за ними число является суммой двух предыдущих.
Представляет собой частный пример линейной рекуррентной последовательности (рекурсии).
"""


# Normal function that returns a list of fibs
def normal_fibonacci(number):
    fibs = [0, 1]

    for i in range(2, number + 1):
        fibs.append(fibs[-1] + fibs[-2])

    return fibs


print('Normal fibs!')
normal_fibs = normal_fibonacci(10)
print(normal_fibs)
print('*' * 20)


# Generator function that returns generator object
def generator_fibonacci(number):
    x_2 = 0
    x_1 = 1

    yield x_2
    yield x_1

    for item in range(2, number + 1):
        yield x_2 + x_1
        x_2, x_1 = x_1, x_2 + x_1


print('Generator fibs!')
generator_fibs = generator_fibonacci(10)

print(next(generator_fibs))
print(next(generator_fibs))
print(next(generator_fibs))
print(next(generator_fibs))
print(next(generator_fibs))
print('*' * 20)


# Same function but generates infinite fibs
def infinite_fibonacci():
    x_2 = 0
    x_1 = 1
    yield x_2
    yield x_1

    while True:
        yield x_2 + x_1
        x_2, x_1 = x_1, x_2 + x_1


infinite_fib = infinite_fibonacci()

print('Infinite fibs!')
print(next(infinite_fib))
print(next(infinite_fib))
print(next(infinite_fib))
print(next(infinite_fib))
print(next(infinite_fib))
print(next(infinite_fib))
print('*' * 20)

print('Infinite fibs for cycle!')
for x in range(10):
    print(next(infinite_fib))
print('*' * 20)
