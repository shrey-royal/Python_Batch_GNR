"""
Dictionary:
    Ordered, Mutable and Unique (no duplicates) collection of pairs containing key and values

-> (Keys must be unique and value may contain duplicates)

"""
from pprint import pprint

# myDict = {
#     "key":"value",
# }
# myDict = dict()
# print(myDict, type(myDict))

# company = {
#     "name": "Kaushal Solutions PVT. LTD.",
#     "address": "Gandhinagar",
#     "turnover": "1000 Cr.",
#     "employees": {
#         "dhruv": (333, "Senior DevOps Engineer", "100 Lac"),
#         "jayal": (14, "CTO", "6.5 Cr."),
#         "vishwas": (7, "CFO", "7 Cr."),
#     },
# }
#
# print(company)
# print(type(company))

#################################################################################

# Dhiraj Sir arranges Royal Jamanvaar for 1 day

Employee_Choice = {
    "Dhiraj Sir" : {"Breakfast" : "Dosa", "Lunch" : "Punjabi", "Dinner" : "khichdi-kadhi"},
    "Zafar Sir" : {"Breakfast" : ['Fafda', 'Jalebi'], "Lunch" : "Kathiyawadi", "Dinner" : "Gujarati"},
    "Shrey Sir" : {"Breakfast" : "Fruits", "Lunch" : "South Indian", "Dinner" : "Maggie"},
    "Madhusudan Sir" : {"Breakfast" : "Solid Masti", "Lunch" : "Pizza", "Dinner" : "Solid Masti"},
}

# Accessing the data
# print(Employee_Choice)

# using square bracket notation (dict[key])
# print(Employee_Choice["Madhusudan Sir"])
# print(Employee_Choice["Zafar Sir"])
# print(Employee_Choice["Krutarth Sir"])  # KeyError

# get() method  # returns None if key not found
# print(Employee_Choice.get("Krutarth Sir"))

# choice = input("Enter the name: ")
# print(Employee_Choice.get(choice, Employee_Choice["Dhiraj Sir"]))

#################################################################################

# add new pairs of data
person = {
    'fname' : 'Cynthia',
    'lname' : 'Wright',
    'age' : 24,
    'favorite_colors' : ['blue', 'green'],
    'aadhaar' : "123-44-7678",
    'active' : True,
}

# person['active'] = False    # add/modifying value
# del person['age']   # deleting pair
# print(person)

for key, value in person.items():
    print(f"{key} : {value}")

# for k, v in person.items():
#     print(f"{k} : {v}")

# Next time dictionary methods