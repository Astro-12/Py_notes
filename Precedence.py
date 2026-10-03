'''
Python follows PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction). The order of operations in Python is:

Parentheses () – Highest precedence, operations inside parentheses are evaluated first.
Exponents ** – Power calculations (e.g., 2 ** 3 → 8).
Multiplication *, Division /, Floor Division //, Modulus % – Evaluated from left to right.
Addition +, Subtraction - – Evaluated from left to right.
'''
##Example:
result = 10 + 2 * 3  # Multiplication happens first: 10 + (2 * 3) = 16
print(result)

result = (10 + 2) * 3  # Parentheses first: (10 + 2) * 3 = 36
print(result)

result = 2 ** 3 ** 2  # Right-to-left exponentiation: 2 ** (3 ** 2) = 2 ** 9 = 512
print(result)
'''
Order of Evaluation
Exponentiation (**) is evaluated right to left.

Example:
print(2 ** 3 ** 2)  # Output: 512
This is evaluated as 2 ** (3 ** 2), meaning 2 ** 9 = 512.
Multiplication (*), division (/), floor division (//), and modulo (%) are evaluated left to right.

Example:
print(16 / 4 * 2)  # Output: 8.0
This is evaluated as (16 / 4) * 2 = 4.0 * 2 = 8.0.
Operator Precedence Summary:
** (Exponentiation) has the highest precedence and is evaluated right to left.
*, /, //, and % have lower precedence than ** but are evaluated left to right.
'''
