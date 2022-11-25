# def generator_squares(number):
#     for i in range(1, number + 1):
#         yield i ** 2
#
#
# generator_sq = generator_squares(10)
# print('Generator squares!')
# print(next(generator_sq))
# print(next(generator_sq))
# print(next(generator_sq))

# from sys import getsizeof
# def normal_fibonacci(number):
#     fibs = [0, 1]
#     for i in range(2, number + 1):
#         fibs.append(fibs[-1] + fibs[-2])
#
#     return fibs
#
# normal_fibs = normal_fibonacci(10)
# print(getsizeof(normal_fibs))
# print(normal_fibs)


# def generator_fibonacci(number):
#     x_2 = 0
#     x_1 = 1
#
#     yield x_2
#     yield x_1
#
#     for item in range(2, number + 1):
#         yield x_2 + x_1
#         x_2, x_1 = x_1, x_2 + x_1
#
# generator_fibs = generator_fibonacci(10)
# print(generator_fibs)
#
# print(next(generator_fibs))
# print(next(generator_fibs))
# print(next(generator_fibs))
# print(next(generator_fibs))
# print(next(generator_fibs))
# print(next(generator_fibs))
# print(next(generator_fibs))

def infinite_fibonacci():
    x_2 = 0
    x_1 = 1
    yield x_2
    yield x_1

    while True:
        yield x_2 + x_1
        x_2, x_1 = x_1, x_2 + x_1


infinite_fibs = infinite_fibonacci()
from sys import getsizeof
print(getsizeof(infinite_fibs))
for i in range(10000):
    print(next(infinite_fibs))


