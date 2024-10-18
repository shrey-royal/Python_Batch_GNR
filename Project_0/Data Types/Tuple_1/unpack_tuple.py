# import random
#
# numbers = [random.randint(0, 100) for _ in range(10)]
# print(numbers)

# the default data type of packing and unpacking is tuple

# n1 = 12, 2345, 8976    # packing tuple
# print(n1)

# _, v1, v2 = n1    # (n1 = 1, n2 = 2, ? = 3)
# print(v1, v2)

nums = (17, 65, 21, 0, 27, 14, 12, 66, 14, 39)
# print("unpack-1: ", end='')
# n1, n2, *n3 = nums   # * will return packed data in list form
# n1, *n2, n3 = nums   # * will return packed data in list form
# *n1, n2, n3 = nums   # * will return packed data in list form
# n1, n2, *_ = nums

print("unpack-2: ", end='')
n1, *n2, n3 = 23, nums, 45

print(n1, n2, n3)