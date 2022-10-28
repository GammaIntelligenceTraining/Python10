x = {'people': {'person1': 'Jack', 'person2': 'Jack'}}
print(type(x))
print(type(x['people']))

y = x['people']['person1']
print(y)

d = [1, 2, 3, ['a', {'name': 'Jack'}, 'c'], 4, 5]

lst = d[1:4]
print(lst)