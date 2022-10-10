# import csv
#
# with open('csv_files/2019.csv', 'r', encoding='utf8') as file:
#     csv_reader = list(csv.DictReader(file))
#     # print(csv_reader)
#
# def sort_values(val):
#     return val['GDP per capita']
#
# csv_reader.sort(key=sort_values, reverse=True)
#
# for line in csv_reader:
#     print(line)

# import csv
#
# with open('csv_files/2019.csv', 'r', encoding='utf8') as file:
#     csv_reader = list(csv.DictReader(file))
#     # print(csv_reader)
#
# csv_reader.sort(key=lambda val: val['GDP per capita'], reverse=True)
#
# for line in csv_reader:
#     print(line)

# x = lambda num1, num2: num1 ** num2
# print(x(10, 2))
# print(x(5, 3))


# sample = [(3, 6, 6), (1, 8, 9), (2, 7, 3)]
# sample.sort()
# print(sample)
# sample.sort(key=lambda x: x[1])
# print(sample)
# sample.sort(key=lambda x: x[2])
# print(sample)
#
# def sort_vals(x):
#     return x[2]
