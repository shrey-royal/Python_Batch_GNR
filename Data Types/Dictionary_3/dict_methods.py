# silly_animals = {
#     "duck" : "Quack",
#     "cat" : "Meow",
#     "dog" : "Woof",
#     "cow" : "Moo",
#     "pig" : "Oink",
#     "lion" : "Roar",
#     "dinosaur" : "RAWR",
# }
# print(silly_animals)

# a = silly_animals.copy()
# silly_animals.clear()
# print(silly_animals)

# new_dict = dict.fromkeys(['a', 'b', 'c', 'd'], 0)
# print(new_dict)

weird_food_pairs = {
    "Peanut Butter" : "Pickle",
    "Pizza" : "Pineapple",
    "Ice Cream" : "Ketchup",
    "Fries" : "Chocolate Sauce",
    "Butter Milk" : "Hershey's Chocolate Syrup",
    "Marie Gold Biscuit" : "Lemon Juice",
    "Milk" : "Pepsi",
    "Bread" : "Ice Cream",
}

# print(weird_food_pairs.get("Fris", "Biscoot"))

# print(weird_food_pairs.items())
# print(weird_food_pairs.keys())
# print(weird_food_pairs.values())

# print(list(weird_food_pairs.items()))
# print(list(weird_food_pairs.keys()))
# print(list(weird_food_pairs.values()))

strange_inventions = {
    "Cat Translator" : "translates meows to human language",
    "Self-tying Shoes" : "Shoes that tie themselves",
    "Invisible Umbrella" : "Protect rain without blocking view",
    "Teleportation Toaster" : "Toasts bread and teleports is to your plate",
    "abcd" : 'abcd'
}

# print(strange_inventions.pop("Invisible Umbrella 2.0", "No such key present!"))
# print(strange_inventions)

# for k, v in strange_inventions.items():
#     print(f"{k} : {v}", end='\n')

# print(strange_inventions.popitem())
# k, v = strange_inventions.popitem()
# print(k, v, sep=': ')

# print(strange_inventions.setdefault("abcd", "xyz"))
strange_inventions.update({"abcd" : None})
print(strange_inventions)

"""
Task

1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Dhruv', 'age' : 24, 'height' : 6.5 , 'job' : 'Businessman', 'company': 'X-Con'}


# HW. Extract Unique Values in a Given Dictionary
# -> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

# D1 = {	
#     'list1': [4, 7, 10, 20], 
#     'list2': [7, 16, 9, 10], 
#     'list3': [13, 10, 4, 8], 
#     'list4': [7, 20, 6, 11]
# }

# Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
"""