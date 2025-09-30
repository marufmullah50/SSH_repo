# Just practicing git and github with SSH

# Initialize local repo
git init

# Create a file
touch index.html

# Edit file in VSCode
code index.html   # (use 'code' not 'vscode')

# Add all files
git add .

# Commit them
git commit -m "Initial commit"

# Connect to GitHub via SSH (replace with your repo SSH link)
git remote add origin git@github.com:your-username/project.git

# Push files (use main if your branch is main)
git push -u origin master




**Calculator Descriptions**

Simple Python Calculator

This is a simple command-line calculator written in Python. It supports basic arithmetic, trigonometry, and calculus operations, and can be used repeatedly until you choose to exit.

Features:
- Arithmetic: Addition, Subtraction, Multiplication, Division
- Trigonometry: sin(x), cos(x), tan(x) (angle input in degrees)
- Calculus: Derivative and Integral (using Sympy)
- Loop Mode: Perform multiple calculations until exit

Requirements:
Make sure you have Python 3 installed.
You will also need sympy for calculus operations:
pip install sympy

Usage:
1. Clone the repository or copy the calculator.py file.
2. Run the calculator:
   python calculator.py
3. Select an operation from the menu:
   1 → Add
   2 → Subtract
   3 → Multiply
   4 → Divide
   5 → Trigonometry
   6 → Calculus
   0 → Exit

Example:
===== Simple Calculator =====
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Trigonometry
6. Calculus
0. Exit
Enter choice: 1
Enter first number: 10
Enter second number: 20
Result: 30

License:
This project is for practice and learning purposes. Free to use and modify.

