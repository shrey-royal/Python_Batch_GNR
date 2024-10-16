# Match Case (Switch Case)

while True:
    print("\n\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting...")
        exit(0)

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    match choice:
        case 1:
            print(f"Addition of {a} and {b} is {a+b}")
        case 2:
            print(f"Subtraction of {a} and {b} is {a-b}")
        case 3:
            print(f"Multiplication of {a} and {b} is {a*b}")
        case 4:
            print(f"Division of {a} and {b} is {a/b}")
        case _:
            print("Invalid choice")

"""
Problem Statement:

You are building a ticket booking system for a cinema. Users can book tickets for different types of movies and seating categories. Implement a `match` case system to handle the following:

1. Movie Types:
   - Action
   - Comedy
   - Drama
   - Horror
   - Science Fiction

2. Seating Categories:
   - Standard
   - Premium
   - VIP

The user should first select the type of movie, then choose the seating category. Based on their 
choices, the system will display the corresponding message and calculate the price based on 
predefined rates:

- Action: $12 (Standard), $18 (Premium), $25 (VIP)
- Comedy: $10 (Standard), $15 (Premium), $20 (VIP)
- Drama: $8 (Standard), $12 (Premium), $18 (VIP)
- Horror: $14 (Standard), $20 (Premium), $27 (VIP)
- Science Fiction: $15 (Standard), $22 (Premium), $30 (VIP)

"""