"""
Functions --> Assistants
=> They are named code blocks that performs a job and may or may not return a value

syntax:
def function_name(parameters):
    \"""
    DocString (optional): A description of what the function does.
    \"""
    # Function Body
    statement(s)
    return value    # optional
"""

# def greet():
#     print("Hello, World!")

# greet()
########################################################################

# def add_numbers(a: int, b: int) -> int:
#     """Returns the sum of two numbers."""
#     return a + b

# print(add_numbers(2, 3))
# print(f"{2} + {3} = {add_numbers(2, 3)}")
########################################################################

# def display_info(name: str, age: int) -> None:
#     print(f"Name: {name}, Age: {age}")

# Positional Arguments
# display_info("Kaushal", 30)

# Keyword Arguments
# display_info(age=34, name="Dhruv")
########################################################################

# Default Arguments
# def greet(name: str = "Guest") -> None:
#     return f"Hello, {name}!"

# print(greet())
# print(greet("Alice"))
########################################################################

# def addition(a: int = 0, b: int = 0) -> int:
#     return a+b

# print(addition(b=78))
########################################################################

# smol praktis
# Problem Statement: Create a function 'greet_user' that takes two parameters: 'name' (a string) and 'greeting' (a string). The greeting parameter should have a default value of "Hello". The function should print a message in the format: "greeting, name!". If no greeting is provided, it should use the default value.
########################################################################

def addition(a: int | float = 0, b = 0) -> None:
    print(f"{a} + {b} = {a+b}")

addition(b=23, a=1)
addition(b=23)