"""
List -> Mutable Sequence

syntax:
    list() -> represented by []

Changeable? -> True
Duplicates Allowed? -> True

"""

#declaration of list
# list_var = list() # using constructors
# list_var = []

# print(list_var, type(list_var), sep="\t")

# initialize lists
# data = ["Apple", 12, 2.3, 's', 1+2j]
# print(data)

# fruits = ["Apple", "Banana", "Cherry", "Dragon Fruit", "Papaya", "Strawberry"]
# prime_nums = list([2, 3, 5, 7, 11, 13, 17, 19, 20-1])

# print(fruits, prime_nums)

# cgpa = [7.8, 7.9, 7.87, 7.26]
# print(cgpa[::-1])

# for i in fruits:
#     print(i[:2])

indian_veggies = [
    "Bitter Gourd (Karela)",
    "Bottle Gourd (Lauki)",
    "Ridge Gourd (Turai)",
    "Snake Gourd (Galka)",
    "Pointed Gourd (Parwal)",
    "Drumstick (Moringa)",
    "Taro Root (Arbi)",
    "Elephant Foot Yam (Suran)",
    "Ash Gourd (Petha)",
    "Ivy Gourd (Tindora)",
    "Fenugreek Leaves (Methi)",
    "Amaranth Leaves (Patra)",
    "Colocasia Leaves (Arbi ke Patte)",
    "Beet Greens (Chukandar ke Patte)",
    "Mustard Greens (Sarson)",
    "Radish Greens (Mooli ke Patte)",
    "Spinach (Palak)",
    "Fenugreek Seeds Sprouts (Methi Dana)",
    "Cluster Beans (Gawar Phali)",
    "French Beans (Hari Faliya)",
    "Yardlong Beans (Bora)",
    "Broad Beans (Sem)",
    "Green Peas (Matar)",
    "Corn (Makai)",
    "Bamboo Shoots (Karil)",
    "Jackfruit (Kathal)",
    "Raw Banana (Kachcha Kela)",
    "Green Papaya (Kachcha Papita)",
    "Indian Gooseberry (Amla)",
    "Curry Leaves (Kadi Patta)",
    "Raw Mango (Keri)",
    "Sponge Gourd (Nenua)",
    "Brinjal (Baingan)",
    "Lady Finger (Bhindi)",
    "Cabbage (Patta Gobi)",
    "Cauliflower (Phool Gobi)",
    "Radish (Mooli)",
    "Turnip (Shalgam)",
    "Carrot (Gajar)",
    "Tomato (Tamatar)"
]

# 1. Get all the veggies with c as a starting letter
# for veggie in indian_veggies:
#     if veggie.lower().startswith('c'):
#         print(veggie)

# 2. Take english input from the user and get the veggie in hindi
# user_input = input("Enter the name of the vegetable in English: ").strip().lower()

# for veggie in indian_veggies:
#     vlist = veggie.split(' (')
#     if user_input == vlist[0].lower():
#         print(vlist[1].replace(')', ''))

# 3. Find all veggies with more than 2 words
# for veggie in indian_veggies:
#     if len(veggie.split()) > 2:
#         print(veggie)

# 4. Find all veggies with only 1 word
# for veggie in indian_veggies:
#     if len(veggie.split()) == 2:
#         print(veggie)

# 5. Find all veggies that contain the word "Gourd"
# 6. List all veggies with their names starting with a vowel
# 7. Count the number of veggies that have Hindi names containing exactly 2 words
# 8. Find all veggies whose English names have exactly 2 words.
# 9. Find all veggies whose Hindi names end with "Patta" (Leaf)
