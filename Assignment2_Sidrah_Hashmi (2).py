#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sidrah Hashmi # 100915053

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def exponentiate(x, y):
    result = 1
    for _ in range(int(y)):
        result *= x
    return result

while True:
    operation = input("Choose an operation (+, -, *, /, ^) or type 'exit' to quit: ").lower()

    if operation == 'exit' or operation == 'stop':
        break

    if operation not in ('+', '-', '*', '/', '^', 'add', 'subtract', 'multiply', 'divide', 'exponentiate'):
        print("Invalid operation. Please try again.")
        continue

    num1 = float(input("Enter the first number: "))

    num2_input = input("Enter the second number or leave it empty to use the previous result: ")

    if num2_input.strip() == '':
        if operation == '^':
            print("For exponentiation, both numbers must be specified.")
            continue
        else:
            num2 = result
    else:
        num2 = float(num2_input)

    if operation in ('+', 'add'):
        result = add(num1, num2)
    elif operation in ('-', 'subtract'):
        result = subtract(num1, num2)
    elif operation in ('*', 'multiply'):
        result = multiply(num1, num2)
    elif operation in ('/', 'divide'):
        result = divide(num1, num2)
    elif operation == '^':
        result = exponentiate(num1, num2)

    print(f"Result: {result}")
    

