"""
getter always gets the @property tag
setter always gets the prop.setter tag
"""

class StreetFood:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    # def __str__(self):  # this method will represent the object in a string format
    #     return f"(name={self.__name}, price={self.__price})"

def main():
    vadapav = StreetFood("vadapav", 20)
    # print(f"Name: {vadapav.name}\nPrice: {vadapav.price}")
    # vadapav.name = "Simple Vadapav"
    # vadapav.price = 25
    # print(f"Name: {vadapav.name}\nPrice: {vadapav.price}")

    items = list()
    items.append(StreetFood('Vadapav', 20))
    items.append(StreetFood('Samosa', 30))

    for item in items:
        print(item.name, ", ", item.price, sep="")


if __name__ == "__main__":
    main()

"""
make one class, name it Vegetables, take name and price(per kg) and make getters and setters for all the attributes and then take a array of veggies and store atleast 7 vegetable objects and print it using getter method 
"""