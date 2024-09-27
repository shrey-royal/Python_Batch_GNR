import list_data as data

var = [data.veggies, data.fruits]
# print(type(var))
# print(type(var[0]))
# print(type(var[0][0]))
# print(var[0][0])
# print(var[1][0])

# for item in var:
#     for j in item:
#         print(j, end=", ")
#     print("\n\n\n")


# for list_item in var:
#     for item in list_item:
#         flatten_list.append(item)

flatten_list = [item for list_item in var for item in list_item]

# print(var)
print(flatten_list)
