# x = 1
# assert x == 2, 'X must be 1'
#


def sum_list(lst: list) -> float:
    assert type(lst) == list, 'Parameter must be of type list'
    assert len(lst), 'Input list is empty'
    total = 0
    for item in lst:
        total += item
    return total

print(sum_list([1, 2, 3, 4, 5, 6]))
# print(sum_list({1: 'one', 2: 'two'}))
# print(sum_list([]))
print(sum_list.__annotations__)

assert len(id) != 11