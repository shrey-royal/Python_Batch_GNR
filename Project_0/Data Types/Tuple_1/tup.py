"""
Tuple -> Immutable Sequence

syntax:
    tuple() -> represented by ()

Changeable? -> False
Duplicates Allowed? -> True

"""

# myTuple = (3, 5, 2, 56, 8, 4, 3, 12, 5, 78, "2", ["2", 34, 2, 2])
# print(myTuple, type(myTuple), id(myTuple))

# print("Index: ", myTuple.index(12, 2, 10))
# print("Len: ", len(myTuple))
# print("Count: ", myTuple.count(2))
# print("Count: ", myTuple[11].count(2))

"""
Example 1:
Ordering tuple by list
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]
"""
# tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
# sortList = ['l', 'a', 'k', 'e']

# output: list = list()
# for k in sortList:
#     for t in tupList:
#         # print(k, t)
#         if k == t[0]:
#             output.append(t)

# output = [t for k in sortList for t in tupList if k == t[0]]
# print(output)

"""
Example 2:
Python program to convert decimal to binary (in bytes)
Input:
tuple1 = (1234, 331, 437, 59, 63)

Output:
(binary of 1, binary of 2, binary of 3, binary of 4, binary of 5)
"""
# using loops -> ?
# print(bin(8)[2:].zfill(8))
tuple1 = (1234, 331, 437, 59, 63)
l = []

for i in tuple1:
    binary = ''
    while i > 0:
        binary = str(i % 2) + binary
        i = i // 2

    while len(binary) < 8:
        binary = '0' + binary

    l.append(binary)

print(tuple(l))