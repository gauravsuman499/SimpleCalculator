
#  a function that takes in two numbers and an operator
def calculate(num1, num2, operator):
    # if the operator is "+", return the result of num1 + num2
    if operator == "+":
        return num1 + num2
    # if the operator is "-", return the result of num1 - num2
    elif operator == "-":
        return num1 - num2
    # if the operator is "*", return the result of num1 * num2
    elif operator == "*":
        return num1 * num2
    # if the operator is "/", return the result of num1 / num2
    elif operator == "/":
        return num1 / num2
    # if the operator is not recognized, return an error message
    else:
        return "Error: Invalid operator"


num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))
# ask the user for the operator
operator = input("Enter the operator (+, -, *, or /): ")

# calculate the result and print it to the screen
result = calculate(num1, num2, operator)
print("The result is:", result)
