num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

match operation:
    case '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    case '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    case '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by 0.")
    case _:
        print("Invalid operation. Please enter +, -, *, or /.")