"""
set - A set is an unordered collections of items, every element should be unique (no duplicates) and mutable means we can change it.

set is mutable(changeable), unordered(no index), no duplicates allowed

syntax -:
mySet = {1, 2, 3, ..., n}
"""

# mySet = {1, 2, 23, 12, 3334, 354, 34, 23, 12, 5, 32}
# print(mySet, type(mySet), sep='\n')

# basics of set
# mySet = {1, 2, 3, "Python", 2.3, 'k'}
# print(mySet)

# set can't have duplicates
# myList = {11, 23, 11, 34, 22, 34, 22, 45, 456, 546, 56, 45, 56}
# print(myList)

# myList = ['veggies', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'chocolates']
# print(set(myList))

# skills = {'Eating', 'Python Programming', 'Patience', 'Vlogging'}
#
# skills.add('Critical Thinking')
# print(skills)
#
# skills.discard('Python Programming')
# print(skills)

mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}

# print(mySet.difference(dummy_set))
# print(mySet - dummy_set)

# mySet.difference_update(dummy_set)
# print(mySet)

# print({1, 2, 3}.isdisjoint({23, 22, 4})) # uniqueness
# print(mySet.intersection(dummy_set))
# mySet.intersection_update(dummy_set)
# print(mySet)
# print(new_set.issubset(dummy_set))
# print(mySet.pop())
# mySet.remove(45)
# print(mySet.symmetric_difference(dummy_set))
# mySet.symmetric_difference_update(dummy_set)
# print(mySet)

# mySet.update((3, 89), [2, 3, 3, 4, 4, 232, 23, 78])
# print(mySet)

# print({1, 2}.union({3, 4}))

# del mySet, dummy_set, disjoint_set, new_set
# print(mySet, dummy_set)

"""
Consider a scenario involving a business with a loyalty program where customers can earn rewards based on certain criteria. 

The program includes:
- Active Customers: Customers currently using the loyalty program.
- Premium Members: Customers who have paid for a premium membership.
- High Spenders: Customers who spend over a certain amount every month.
- Discount Eligible Customers: Customers who can receive discounts based on their spending patterns.

In this scenario, let's say we want to:
1. Find customers who are both active and premium members.
2. Identify high spenders who are not premium members (to encourage them to join the premium membership).
3. Find customers eligible for discounts who are also high spenders.
4. Get the list of all customers in any of these categories without duplicates.

# Defining sets for each category
active_customers = {"Alice", "Bob", "Carol", "David", "Eve"}
premium_members = {"Bob", "Carol", "Frank", "Grace"}
high_spenders = {"Alice", "David", "Eve", "Frank"}
discount_eligible = {"Bob", "Eve", "Grace", "Henry"}
"""