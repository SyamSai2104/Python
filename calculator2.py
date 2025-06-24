def calculate():
    """Simple calculator with basic operations and error handling."""
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b,
    }

    print("Simple Calculator")
    print("Operations: +, -, *, /, ^ (power)")
    print("Enter 'exit' to quit\n")

    while True:
        try:
            # Get first number
            num1_input = input("Enter first number (or 'exit'): ")
            if num1_input.lower() == 'exit':
                print("Goodbye!")
                return
            num1 = float(num1_input)
            
            # Get operation
            op = input("Enter operation: ")
            if op.lower() == 'exit':
                print("Goodbye!")
                return
            if op not in operations:
                print("Invalid operation! Please use: +, -, *, /, ^")
                continue
            
            # Get second number
            num2_input = input("Enter second number (or 'exit'): ")
            if num2_input.lower() == 'exit':
                print("Goodbye!")
                return
            num2 = float(num2_input)
            
            # Special case for division by zero
            if op == '/' and num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
                
            # Perform calculation
            result = operations[op](num1, num2)
            print(f"Result: {num1} {op} {num2} = {result}\n")
            
        except ValueError:
            print("Invalid number input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate()