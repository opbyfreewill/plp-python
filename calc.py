num1 = float(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on user input
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Print the result
print(f"{num1} {operator} {num2} = {result}")
