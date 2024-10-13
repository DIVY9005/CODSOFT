# Function to perform the chosen operation
def calculator():
    print("Simple Calculator")
    
    # Get user input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Get user's choice for the operation
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform the operation based on the user's choice
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input. Please choose a valid operation.")

# Call the calculator function
calculator()
