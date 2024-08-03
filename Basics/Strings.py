"""
# String declaration

name = "Kaushal"
message = 'Hello, Kaushal'

# f_ormatted string (fstring)

message = f"Good evening, {name}"
# print(message)

greetings = 'Good' ' Morning!' ' Jay' # concatenation

greeting = 'Good '
time = 'Evening'

msg = greeting + time + "!"

print(msg)

#--------------------------------------------------------------

# Accessing String elements

# str = None

str = 'Python String'
print(str[0])
print(str[12])

print(len(str))

print(str[-13])
print(str[12])

#--------------------------------------------------------------

# Slicing - a TECHNIQUE that helps in extraction of specific words/parts of string.

# syntax: SEQUENCE[start(inclusive):end(exclusive):step-1]
# start (0) -> index from which it will start extracting your string
# end (len_of_sequence) -> till this index it will extract the string (the end index is exclusive)
# step (1) -> number that tells the interpreter how many characters to skip

# positive/negative

word = "Artificial_Intelligence"

# Positive Slicing

# print(word[0:4])
# print(word[4:10])

'''
# smol praktis
new_word = word[:4] + '-' + word[4:10]
new_word = f'{word[:4]}-{word[4:10]}'
print(new_word)
'''

'''
# Another example
pasta = "Pasta_Alla_Norma"
two = pasta[6:10]
three = pasta[11:]
print(two, three, sep='\n')
'''

# Step - skip characters

word = "0_1_2_3_4_5_6_7_8_9"

print(word[::3])    # step = 2 (working: step-1)
print(word[::4])    # even
print(word[2::4])   # odd
"""

#--------------------------------------------------------------

# Negative Slicing (reverse reading of any iterable data)
