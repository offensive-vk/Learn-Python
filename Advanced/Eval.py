def evaluate_expression(expression):
    try:
        result = eval(expression)
        print(f"Result of '{expression}': {result}")
    except Exception as e:
        print(f"Error evaluating expression '{expression}': {e}")

# Example 1: Simple arithmetic
evaluate_expression('2 + 3 * 4')

# Example 2: Using variables
x = 5
evaluate_expression('x ** 2 + 3 * x - 7')

# Example 3: Trigonometric functions
import math
evaluate_expression('math.sin(math.radians(30))')

# Example 4: User input
user_input = input("Enter a mathematical expression: ")
evaluate_expression(user_input)
