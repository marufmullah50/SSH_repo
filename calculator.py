# Simple Calculator in Python
# Features: Arithmetic, Trigonometry, Calculus, Reset option

import math
import sympy as sp

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def trig_operations():
    print("\nTrigonometry:")
    print("1. sin(x)")
    print("2. cos(x)")
    print("3. tan(x)")
    choice = input("Choose operation (1/2/3): ")
    angle = float(input("Enter angle in degrees: "))
    rad = math.radians(angle)
    if choice == '1':
        return math.sin(rad)
    elif choice == '2':
        return math.cos(rad)
    elif choice == '3':
        return math.tan(rad)
    else:
        return "Invalid choice"

def calculus_operations():
    print("\nCalculus:")
    x = sp.symbols('x')
    expr = sp.sympify(input("Enter expression in terms of x (e.g., x**2 + 3*x): "))
    print("1. Derivative")
    print("2. Integral")
    choice = input("Choose operation (1/2): ")
    if choice == '1':
        return sp.diff(expr, x)
    elif choice == '2':
        return sp.integrate(expr, x)
    else:
        return "Invalid choice"

# Main loop
while True:
    print("\n===== Simple Calculator =====")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Trigonometry")
    print("6. Calculus")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == '0':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

    elif choice == '5':
        print("Result:", trig_operations())

    elif choice == '6':
        print("Result:", calculus_operations())

    else:
        print("Invalid input! Please try again.")

    # Reset option
    reset = input("\nDo you want to perform another calculation? (y/n): ")
    if reset.lower() != 'y':
        print("Exiting calculator. Goodbye!")
        break
