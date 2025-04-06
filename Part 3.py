# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is even or odd and print the appropriate message
if is_even(number):
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
