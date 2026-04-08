# EX3

# def normalizeaza(lista):
#     mini, maxi = min(lista), max(lista)
#     return [(x - mini) / (maxi - mini) for x in lista]

# date = [10, 20, 30, 40, 50]
# print(normalizeaza(date))

# EX4
# x=[1,2,3,4,5]
# patrat = lambda x: x**2
# elementepatrat= list(map(patrat,x))
# print(elementepatrat)

# EX5
# sort_lambda = lambda lst: sorted(lst, key=lambda x: x[1])
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# print(sort_lambda(a))

# EX6
# orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_list = list(filter(lambda x: x % 2 == 0, orig_list))
# odd_list = list(filter(lambda x: x % 2 != 0, orig_list))
# print("Lista originala:", orig_list)
# print("Numere pare:", even_list)
# print("Numere impare:", odd_list)

# EX7
# preturi = [100, None, 200, None, 300]
# preturi_filtrate = list(filter(lambda x: x is not None, preturi))
# preturi_reducere = list(map(lambda x: x * 0.9, preturi_filtrate))
# print("Preturi filtrate:", preturi_filtrate)
# print("Preturi cu reducere 10%:", preturi_reducere)

# EX8
# extract_date_time = lambda s: (s[:4], s[5:7], s[8:10], s[11:])
# example = "2023-04-24 09:03:32"
# year, month, day, time = extract_date_time(example)
# print(year)
# print(month)
# print(day)
# print(time)

# EX9
# list3 = []
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]

# def sum_lists(list1, list2):
#     for i, j in zip(list1, list2):
#         list3.append(i + j)
#     return list3

# print(sum_lists(list1, list2))

# EX10
# even_numbers = [x for x in range(101) if x % 2 == 0]
# print(even_numbers)

# cubes = [x**3 for x in range(10)]
# print(cubes)

# list_a = [1, 2, 3, 4, 5]
# list_b = [3, 4, 5, 6, 7]
# common_elements = [x for x in list_a if x in list_b]
# print(common_elements)

# EX11
# SET1 = {x for x in range(11) if x % 2 == 0}
# print(SET1)

# string = "hello world"
# distinct_letters = {x for x in string if x != " "}
# print(distinct_letters)

# text = "ana are mere gustoase"
# words_5_letters = {word for word in text.split() if len(word) >= 5}
# print(words_5_letters)

# EX12
# squares = {x: x**2 for x in range(1, 11)}
# print(squares)

# string = "hello world"
# letter_count = {char: string.count(char) for char in set(string) if char != " "}
# print(letter_count)

# divisors = {x: [d for d in range(1, x+1) if x % d == 0] for x in range(1, 11)}
# print(divisors)


