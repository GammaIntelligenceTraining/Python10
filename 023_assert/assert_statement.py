# Nothing happens because condition
# evaluated to True
x = 1
assert x == 1

# # Will rais AssertionError
# x = 2
# assert x == 1

# # Will rais AssertionError
# x = 2
# assert x == 1, 'X should be 1'


# -> arrow is a comment for function return
# also function arguments can be annotated
def sum_list(s: 'in km', t: 'in hours') -> 'kmh':
    return s/t


print(sum_list(10, 2))
print(sum_list.__annotations__)


# function without assert statement
def sum_list(lst: list) -> float:
    total = 0
    for item in lst:
        total += item

    return total


# assert statement inside function
def sum_list(lst: list) -> float:
    assert type(lst) == list, 'Param lst must be of type list!'
    assert len(lst), 'Input list is empty'
    total = 0
    for item in lst:
        total += item

    return total


# # Both these calls will raise assertion error
# print(sum_list({1: 'One', 2: 'Two'}))
# print(sum_list([]))

# Works fine if filled list provided
print(sum_list([1, 2, 3, 4, 5]))