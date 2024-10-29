num1 = float(input("Enter a number: ")) 
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
  print(num1 + num2)
elif op == "-":
  print(num1 - num2)
elif op == "/":
  print(num1 / num2)
elif op == "*":
  print(num1 * num2)
else:
  print(f"{op} is an invalid operator")