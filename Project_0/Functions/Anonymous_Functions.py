"""
Lambda Functions: A function without a name is called lambda/anonymous function
syntax:
    lambda arguments: expression
"""

# Traditional example
# def add(x, y):
#     return x+y

# add_lambda = lambda x, y: x+y

# print(add(5, 10))
# print(add_lambda(5, 10))
#################################################

# square = lambda x: x ** 2
# print(square(7))
#################################################

# add = lambda a=10, b=100: a+b
# print(add())
#################################################

# parameterless lambda functions
# greet = lambda : "Hello!"
# print(greet())
#################################################

# inline lambda
# print((lambda x: x*x*x)(3))
# -----------------------------------------------------------------------------------------

import random
#
# pairs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]
# print(pairs)

# map(function, iterable) -> used to process data (work with any function who returns some data)

# Normal
# def map_func(elem):
#     return elem[0]*elem[1]

# mappedList = list(map(map_func, pairs))
# mappedList = list(map(lambda elem: elem[0] * elem[1], pairs)) # lambda
# print(mappedList)
#################################################

# numbers = [1, 2, 3, 4, 5]
# squares = list(map(lambda x: x*x, numbers))
# print(squares)
# -----------------------------------------------------------------------------------------

# filter(function, iterable) -> used with boolean function

# Normal
# def filter_func(elem):
#     # max_elem = max(elem[0], elem[1])
#     return elem[0] > 7

# filtered_list = list(filter(filter_func, pairs))
# filtered_list = list(filter(lambda elem: elem[0] > 5, pairs))    # lambda
# print(filtered_list)
# -----------------------------------------------------------------------------------------

# sorted()
# myList = [67, 56, 43, 23, 435, 456, 67, 3, 23, 23, 2]
# print(myList, sorted(myList), sep="\n")
# sortedList = list(filter(lambda x: x%2 == 0, sorted(myList)))
# sortedList = sorted(myList, key=lambda x: -x)

# sortedList = sorted(pairs, key=lambda x: x[0])
# print(sortedList)

# fruits = [(1, '🍉'), (2, '🍒'), (3, '🍎'), (4, '🍅')]
# sortedFruits = sorted(fruits, key=lambda x: -x[0])
# print(sortedFruits)

# num_list = [23, 345, 234, 56, 23, 45, 567]
# s1 = sorted(num_list, key=lambda x: x)
# s2 = sorted(num_list, key=lambda x: x%10)
# print(s1)
# print(s2)
# -----------------------------------------------------------------------------------------

# reduce(function, sequence, initializer(optional)): apply function on all elems of sequence
# from functools import reduce

# def max(a, b):
#     return a if a>b else b

# myList = [211, 4, 6, 8, 10, 11]
# print(reduce(max, myList))
# pairs = [random.randint(0, 10) for _ in range(5)]
# print(pairs)
# print(reduce(lambda x, y: x*y, pairs))

# any method requires any single elements in order to return True
# print(any([False, False, False, False]))    # returns false as all elems are false
# print(any([False, True, False, False]))     # Here the method will short-circuit at the second item (True) and will return true

# all method requires all the elements in order to return True
# print(all([False, False, False, False]))
# print(all([False, False, False, True]))
# print(all([True, True, True, True]))
# print(all([True, False, True, True]))

multiple_of_6 = list(not (i % 6) for i in range(1, 10))
print(multiple_of_6)
print(any(multiple_of_6))   # or
print(all(multiple_of_6))   # and

