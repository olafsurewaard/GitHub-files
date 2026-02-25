print("hello2")

def add_three_numbers(a, b, c):
    return a + b + c

print("hello2")

# Get user input for three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Call the function to add them
result = add_three_numbers(num1, num2, num3)
print(f"{int(num1)} + {int(num2)} + {int(num3)} = {int(result)}")
