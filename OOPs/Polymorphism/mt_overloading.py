# Using default arguments
# class MyClass:
#     def greet(self, name="Guest"):
#         print(f"Hello, {name}")

# obj = MyClass()
# obj.greet()
# obj.greet("Kaushal")

# Using type checking:
# class MyClass:
#     def display(self, arg):
#         if isinstance(arg, str):
#             print(f"String: {arg}")
#         elif isinstance(arg, int):
#             print(f"Integer: {arg}")
#         else:
#             print("Unknown type")

# obj = MyClass()
# obj.display("Hello")
# obj.display(10)
# obj.display([1, 2, 3, 4])

# --------------------------------------------------------------------

class AreaCalculator:
    def area(self, radius=None, length=None, width=None):
        if radius is not None:
            return 3.14 * radius * radius
        elif length is not None and width is not None:
            return length * width
        else:
            raise ValueError("Invalid parameters!")
        
def main():
    calc = AreaCalculator()
    print(calc.area(radius=5))
    print(calc.area(length=4, width=6))

if __name__ == "__main__":
    main()