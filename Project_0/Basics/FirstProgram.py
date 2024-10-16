# single line comment
'''
multi
line
comment
'''
"""
multi
line
comment
"""
'''
print statement:
syntax:
    (*objects, sep=' ', end="\n") -> None
'''

# print("Hello, World!", end='')
# print("This is an object", '\t', "this is another object", 123, '\n', 'this is the third object')

# print("Apple", "Banana", "Cherry", sep='\t') # sep is seperator which will seperate the objects
# print("Apple", "Banana", "Cherry", sep='\t', end='\\') # end 

# Data Types
"""

1. Text: str
2. Numeric: int, float, complex(117j)
3. Sequence: list, tuple, range
4. Mapping: dict
5. Set: set, frozenset
6. Boolean: bool
7. Binary: bytes(binary), bytearray(array of binary nums)
8. None: NoneType
"""

# print("\"Hello, World!\"")
# print("""Hello 
#       wedsiofhweruibgjkeruig
#       rth
#       rt
#       hrty
#       hrty
#       hj
#       rhj
#       hrty
#       hjt
#       j
#       tj
#       tyu
#       World!""")
# print("\"\"\"Hello World!\"\"\"")

# print("dergedfg"+
#       "dsg"+
#       "dfsg"+
#       "sdfg"+
#       'dsf'+
#       'globalgd'+
#       "FloatingPointErrordfg"+
#       'defgdf'+
#       'g')

# id, type
# id() -> used to verify the identity of any variable
# type() -> used to identify the data type (return classes)

# Variables

# a = "This is String"
# print(a, id(a), sep=' -> ')

# b = a
# print(a, b, id(a), id(b), sep='\n')
# a = "abcd"
# b = "xyz"
# print(a, b, id(a), id(b), sep='\n')

# c = "This is String"
# print(c, id(c), sep=' -> ')


# a = "strr"
# print("a = ", a, "\nid = ", id(a), "\ntype = ", type(a))
# print("a = " + str(a) + "\nid = " + str(id(a)) + "\ntype = " + str(type(a)))
# print(f"a = {a}\nid = {id(a)}\ntype = {type(a)}")

# a = 12                # int
# a = 12.2              # float
# a = 1-12j             # complex
# a = "name"            # str
# a = True  # False     # bool (True/False)
# a = b'01'             # bytes
a = None                # None

print(f"{id(a)} -> {type(a)} -> {a}")