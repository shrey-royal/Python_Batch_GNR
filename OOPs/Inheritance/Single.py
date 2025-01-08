class Vehicle:  # parent class
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        return f"Brand: {self.brand}"
    
class Car(Vehicle):     # child class
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_details(self):
        return f"{super().display_brand()}, Model: {self.model}"
    
def main():
    c = Car("Maruti Suzuki", "Omni")
    print(c.display_details())

if __name__ == "__main__":
    main()


"""
-> Problem Statement: Library Management System for E-Books

-> Objective
Develop a Library Management System (LMS) that allows librarians to manage physical books and e-books effectively, focusing on their unique attributes.

-> Requirements

1. Class Structure:
   - Base Class: `Book`
     - Attributes: `title`, `author`
     - Method: `display_info()`
   - Derived Class: `EBook` (inherits from `Book`)
     - Additional Attribute: `file_size`
     - Method: `display_ebook_info()`

2. Functionality:
   - Add new physical books and e-books.
   - View details of both types of books.
   - Utilize inheritance to extend functionality.

3. User Interaction:
   - Console-based interface for adding and viewing books.
   - Basic input validation (e.g., positive file size).
"""