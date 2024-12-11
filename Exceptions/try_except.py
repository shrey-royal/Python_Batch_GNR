"""
# try...except -> statement
There are mainly two kinds of errors: syntax errors and exceptions
"""

# print("Before Exception")

# a = int(input("Enter int: "))
# print(a)

# print("After Exception")

# Example - sales growth
# print('Enter the net sales for')

# previous = float(input('- Prior period: '))
# current = float(input('- Current period: '))

# change = (current - previous) * 100 / previous

# if change > 0:
#     result = f'Sales increase {abs(change)}%'
# else:
#     result = f'Sales decrease {abs(change)}%'

# print(result)

# -------------------------------------------------------------
# Handling the exception

# try:
#     print('Enter the net sales for')

#     previous = float(input('- Prior period: '))
#     current = float(input('- Current period: '))

#     change = (current - previous) * 100 / previous

#     if change > 0:
#         result = f'Sales increase {abs(change)}%'
#     else:
#         result = f'Sales decrease {abs(change)}%'

# except:
#     print('Error! Please enter a number for net sales.')

# -------------------------------------------------------------------------
# Catching Custom Exception

print("Before Exception")

try:
    print('Enter the net sales for')

    previous = float(input('- Prior period: '))
    current = float(input('- Current period: '))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increase {abs(change)}%'
    else:
        result = f'Sales decrease {abs(change)}%'

    print(result)

# except ValueError:
#     print('Error! Please enter a number for net sales.')

# except ZeroDivisionError:
#     print('Error! The prior net sales cannot be zero.')

# except (ValueError, ZeroDivisionError) as error:
#     print(f"Error! -> {error}")

except Exception as e:  # general errors / other exceptions
    print(e)

print("After Exception")