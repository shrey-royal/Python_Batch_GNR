"""
Public AM (default): accessible from outside
Protected AM (_): Intended for internal use or subclasses
Private AM (__): Not meant to be accessed from outside the class
"""

class Counter:
    def __init__(self):
        self.__current = 0  # private attribute

    def increment(self):
        self.__current += 1

    def value(self):
        return self.__current
    
    def reset(self):
        self.__current = 0

def main():
    c = Counter()

    c.increment()
    c.increment()
    c.increment()

    print(c.value())

if __name__ == "__main__":
    main()