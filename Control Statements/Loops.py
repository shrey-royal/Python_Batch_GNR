'''
Loop: Entry-Controlled Loop

1. for: fixed iteration
syntax:
    for iterator_var in iterable:
        # body

2. while: unfixed iteration
syntax:
    while condition:
        # body

'''

# range(start=0 (optional), stop (n-1), step=1 (optional)) function

# for i in range(1, 10):
#     print(i, end=', ')

# user_input = int(input("Enter the end: "))

# for i in range(user_input):
#     print(i, end=', ')
# print("\b\b.")

# for i in range(0, 20, 2):
#     print(i, end=', ')
# print("\b\b.")

i = 1
while i<=10:
    print(i, end=', ')
    i += 1
print('\b\b.')