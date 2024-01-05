# Please note that using eval() with user input can be risky, so be cautious and consider input validation in a real-world scenario.
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

# ==============================
def calculator():
    while True:
        try:
            user_input = input("Enter a mathematical expression (or 'exit' to quit): ")

            # Check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Calculator exiting. Goodbye!")
                break

            result = eval(user_input)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    calculator()
