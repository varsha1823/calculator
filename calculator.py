def calculate(num1, num2, operator):
  """
  Performs basic arithmetic operations based on the provided operator.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the calculation.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator")
    return None

# Get user input
while True:
  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

# Get operation choice
while True:
  operator = input("Choose operation (+, -, *, /): ")
  if operator in "+-*/":
    break
  else:
    print("Invalid operator. Please choose +, -, *, or /.")

# Perform calculation and display result
result = calculate(num1, num2, operator)
if result is not None:
  print("Result:", result)
