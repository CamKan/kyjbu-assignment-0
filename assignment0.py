# Function to add two numbers
def add_two_numbers(num1, num2):
    return num1 + num2

# Input: Prompt user to enter two numbers
number1 = int(input("Enter the first integer number: "))
number2 = int(input("Enter the second integer number: "))

# Calculate the sum
sum_result = add_two_numbers(number1, number2)

# Output: Print the sum to the command line
print(f"The sum of {number1} and {number2} is {sum_result}")
