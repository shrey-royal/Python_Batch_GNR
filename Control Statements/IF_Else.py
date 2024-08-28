"""
Conditional Statements:

1. Using branching

if this than that

age > 18 : print("Adult")
age < 18 : print("kid")


-> if statement
-> match case

2. Using looping:

-> for loop
-> while loop
-------------------------------------


if condition:
    //
else:
    //

4 types of if else statement
    -> if statement
        if condition:
            //statement

    -> if else statement
        if condition:
            //statement
        else:
            //statement
    
    -> ladder if statement
        if condition:
            //statement
        elif condition:
            //statement
        elif condition:
            //statement
        else:   # default
            //statement
    
    -> nested if
        if condition:
            # nested if statement
            if condition:
                //statement
            else:
                //statement
        else:
            //statement
    
python does not have switch case.
we have match case instead.
"""

age = int(input("Enter your age: "))

if age > 0 and age < 100:
    if age <= 18:
        print("Kid")
    elif age <= 60: # else if
        print("Adult")
    else:
        print("Senior Citizen")
else:
    print("Invalid Age")