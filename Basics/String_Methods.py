# text = "helLo World!"
# print(len(text))
# print(text.capitalize())
# print(text.casefold() == "hello world!")
# print(text.count('l'))
# print(text.center(len(text)+10, '-'))
# print('cāf𐌄'.encode(encoding='ASCII', errors='xmlcharrefreplace'))

# text = "python programming is fun"
# print(text.endswith('is fun'))
# print("Hello\tWorld".expandtabs(10))

# print("hello world".find('o', 0, 3))
# print("python programming".find('Prog'))  # returns -1

# text = "Good {}!"
# print(text.format("Evening"))
# print("Addition of {} and {} is {}".format(5, 3, 5+3))
# print("{2}, {0}, {3} and {1} are learing python with me.".format("Archi", "Herry", "Dhruv", "Yug"))

# print("hello world".index('_'))     # returns ValueError
# print("HELLO124".isupper())
# print("hello124".islower())
# print("hellO".isalpha())
# print("hello123".isalnum())
# print("D#ruv".isascii())
# print("2²".isdigit())
# print("2²".isdecimal())
# print("234".isnumeric())
# print("_var".isidentifier())
# print("cafē\n".isprintable())
# print("     ".isspace())
# print("   Hello World".istitle())
# print(" ".join('ABC'))
# print("'", "hello".ljust(10, '-'), "'", sep="")
# print("-*-*-*-*-*-|*-*-*-*-*-*-*-hello".lstrip('*-'))

# string = "royal technosoft pvt. ltd."
# table = str.maketrans("ot", "0😊")
# print(table)
# print(string.translate(table))

# print("royal technosoft".partition("tech"))
# print("royal technosoft".partition(" "))
# print("royal technosoft".partition("o"))
# print("royal technosoft".partition(""))     # ValueError: empty separator
# print("royal technosoft".partition("@"))
# print("royal technosoft".partition("ft"))

# print("royal technosoft".replace("tech", "TECH"))
# print("royal technosoft".replace("tech", ""))

# print("'", "royal technosoft  m      ".rstrip(" "), "'", sep='')
# print("royal technosoft".removeprefix("ro"))
# print("royal technosoft".removesuffix("nosoft"))
# print("royal technosoft".rfind("o"))
# print("royal technosoft".rindex("e"))
# print("'", "royal technosoft".rjust(50), "'", sep="")
# print("royal technosoft".rsplit("o"))
# print("royal technosoft".rpartition("o"))

# print("royal technosoft".startswith("roy"))
# print("royal Technosoft".split("o"))
# print("Lorem ipsum \ndolor sit amet consectetur \n\nadipisicing elit. Error iusto, quam culpa odit non, quae, facilis perspiciatis praesentium optio possimus nisi totam? ".splitlines())
# print("^^^^^^^^^^^^^^-^^---$-----^^----^-0----&--------Kaushal Patel-^^---$-----^^----^-0----&--------^^^^^^^^^^^^".strip("-^$"))
# print("KauShAl Patel".swapcase())

# print("kAUSHAL patel".title())
# print("kaushal Patel".upper())
print("11001".zfill(8))