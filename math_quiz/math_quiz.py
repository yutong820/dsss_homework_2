import random


def random_num(min, max):
    """
    Create a random number between min and max value.
    
    Returns:
        A random number between min and max value.
    """
    return random.randint(min, max)


def random_operator():
    """
    Select a random mathematical operator.

    Returns:
        A string which indicates a certain random operator.
    """
    return random.choice(['+', '-', '*'])


def mathOperator_path(num1, num2, operator):
    """
    Create a math problem using two numbers and an operator.

    Args:
        num1: The first number.
        num2: The second number.
        operator: The mathematical operator.

    Returns:
        A tuple containing a string representation of the problem and the correct result.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return problem, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
         num1 = random_num(1, 10)
         num2 = random_num(1, 10)
         operator = random_operator()

         PROBLEM, RESULT = mathOperator_path(num1, num2, operator)
         print(f"\nQuestion: {PROBLEM}")
        
         # Error handling for user input
         try:
             user_RESULT = int(input("Your RESULT: "))
            
             if user_RESULT == RESULT:
                print("Correct! You earned a point.")
                score += 1
             else:
                 print(f"Wrong answer. The correct result is {RESULT}.")
        
         except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
