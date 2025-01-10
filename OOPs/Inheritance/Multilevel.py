class GrandFather:
    def __init__(self, name):
        self.name = name

class Father(GrandFather):
    def __init__(self, name):
        super().__init__(name)
        self.property = 100000

class Child(Father):
    def __init__(self, name):
        super().__init__(name)

    def getHeritage(self):
        return f"{self.name} is a child and his father has the property over {self.property} millions."

def main():
    c = Child("Kaushal")

    print(c.getHeritage())

if __name__ == "__main__":
    main()


"""
Task: 

-> Problem Statement: Library Management System with Multilevel Inheritance

- Background
As libraries expand their collections, managing different categories of books becomes essential. A Library Management System (LMS) is needed to handle various types of books, including physical books and e-books, while utilizing multilevel inheritance to organize the relationships between these classes.

- Objective
Create a Library Management System that employs multilevel inheritance to manage physical books, e-books, and a specialized category of reference books.

- Requirements

1. Class Structure:
   - Base Class: `Book`
     - Attributes: `title`, `author`
     - Method: `display_info()`
   - Intermediate Class: `EBook` (inherits from `Book`)
     - Additional Attribute: `file_size`
     - Method: `display_ebook_info()`
   - Derived Class: `ReferenceBook` (inherits from `EBook`)
     - Additional Attribute: `reference_number`
     - Method: `display_reference_info()` that displays reference-specific details.

2. Functionality:
   - Add new physical books, e-books, and reference books.
   - View details for each type of book, showcasing inherited and unique attributes.
   - Ensure that each derived class can access methods from its parent classes.

3. User Interaction:
   - Implement a console-based interface for adding and viewing books.
   - Include basic input validation for attributes like file size and reference number.
"""