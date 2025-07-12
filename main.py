"""
Simple Calculator Program
This program performs basic arithmetic operations (+, -, *, /) on two user-input numbers.
"""

try:
    # Get the first number from user input
    first_number = int(input("Enter the first number: "))
    
    # Get the second number from user input
    second_number = int(input("Enter the second number: "))
    
    # Display available operations to the user
    print("What kind of operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction") 
    print("Press / for division")
    print("Press * for multiplication")
    
    # Get the operation choice from user
    operation = input("Enter Operation: ")
    
    # Perform the selected operation using match-case statement
    match operation:
        case "+":
            result = first_number + second_number
            print(f"The result is: {result}")
        case "-":
            result = first_number - second_number
            print(f"The result is: {result}")
        case "*":
            result = first_number * second_number
            print(f"The result is: {result}")
        case "/":
            # Check for division by zero
            if second_number == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = first_number / second_number
                print(f"The result is: {result}")
        case _:  # Default case for invalid operations
            print("Error: Invalid operation selected. Please use +, -, *, or /")

except ValueError:
    # Handle invalid input (non-numeric values)
    print("Error: Please enter valid numeric values for both numbers.")
except Exception as e:
    # Handle any other unexpected errors
    print(f"An unexpected error occurred: {e}")
