class Animal:
    def make_sound(self):
        return "Some generic animal sound"
    
class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
def main():
    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.make_sound())

if __name__ == "__main__":
    main()