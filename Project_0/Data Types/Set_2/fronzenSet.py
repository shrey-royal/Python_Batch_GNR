"""
frozenset - immutable and constants
when a fronzenset is declared then it can't be changed
"""

# set1 = frozenset({1, 23, 56, 78, 34, 89, 234})
# print(set1, type(set1))

# name = frozenset({'D', 'h', 'r', 'u', 'v'}) # unordered
# print(name)

# s1 = {'D', 'h', 'r', 'u', 'v'}
# print(s1, type(s1))
list1 = list([1, 2, 3, 4, 5, 6])
fs = frozenset(list1)
# print(fs)

# fs_union = fs.union([4, 5, 6, 7])
# fs_intersection = fs.intersection([2, 3, 14, 5])
# print(fs_union)
# print(fs_intersection)

print(frozenset({1, 2, 3, 4}) | frozenset([2, 3, 4, 5]))
print(frozenset({1, 2, 3, 4}) & frozenset([2, 3, 4, 5]))

# fs.add(6)       # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(4)    # AttributeError: 'frozenset' object has no attribute 'remove'