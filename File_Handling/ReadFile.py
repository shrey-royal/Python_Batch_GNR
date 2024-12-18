"""
file opening modes:
'w' - write
'r' - read
'a' - append
'w+/r+' - write and read
"""

# with open("filename.extension", "mode")

from pprint import pprint
"""
with open("abc.txt", "r") as f:
    # lines = f.read()  # this will scan whole file as string
    # lines = f.readline()    # this will read only single line
    lines = f.readlines()    # this will read only single line

pprint([line.strip() for line in lines if line.strip() != ''], indent=5)
"""

# Default encoding = ASCII
with open("japanese.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()

pprint([line.strip() for line in lines if line != ''] , indent=5)