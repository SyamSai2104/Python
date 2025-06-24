class Calculator():
    def __init__(self, *nums):
        self.nums = nums

    def sum_of_nums(self):
        return sum(self.nums)
    
    def sub_of_nums(self):
        if not self.nums:
            return 0
        result = self.nums[0]
        for num in self.nums[1:]:
            result -= num
        return result

    def mul_of_nums(self):
        if not self.nums:
            return 0
        result = self.nums[0]
        for num in self.nums[1:]:
            result *= num
        return result

    def div_of_nums(self):
        if not self.nums:
            return 0
        result = self.nums[0]
        for num in self.nums[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero")
            result /= num
        return result
def get_numbers():
    numbers = []
    while True:
        try:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            numbers.append(float(num))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers

def main():
    print("Welcome to the Multi-Value Calculator!")
    numbers = get_numbers()
    if not numbers:
        print("No numbers entered. Exiting...")
        return

    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    option = input("Enter an operator (+, -, *, /): ")
    
    calc = Calculator(*numbers)
    if option == "+":
        result = calc.sum_of_nums()
    elif option == "-":
        result = calc.sub_of_nums()
    elif option == "*":
        result = calc.mul_of_nums()
    elif option == "/":
        try:
            result = calc.div_of_nums()
        except ValueError as e:
            print(e)
            return
    else:
        print("Enter a valid operator")
        return
    print(numbers)
    print(option)
    print(result)

if __name__ == "__main__":
    main()
    