"""
# *args -> arguments

# val = 1, 2, 3, 4, 5     # packing
# print(val, type(val))

def add(*args):
    print(args, type(args), sep=' ')
    return sum(args)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(add(1, 2, *[3, 4, 5], 6, 7, 8, 9, 10))
"""
#########################################################################
# **kwargs -> keyword arguments

def connect(**connection_info):
    print(connection_info, type(connection_info))

# connect(server='localhost', port=8080, user='admin', password='root')

# config = {'server': 'localhost', 'port': 8080, 'user': 'admin', 'password': 'root'}
# connect(**config)
connect(connection_info = [1, 2, 3])