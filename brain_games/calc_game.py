def play_calc_game():
    from random import choice, randint

    from prompt import string

    from brain_games import engine

    name = engine.greet_and_get_name()
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        operator = choice(operators)
        number1, number2 = randint(0, 25), randint(0, 25)
        print(f'Question: {number1} {operator} {number2}')
        answer = int(string("Your answer: "))
        correct_answer = get_correct_answer(number1, number2, operator)
        i = engine.check_answer(answer, correct_answer, i)
    if i == 4:
        print(f"'{answer}' is wrong answer ;(. Correct answer was " + 
            f"'{correct_answer}'.")
        print(f"Let's try again, {name}!")
    if i == 3:
        print(f'Congratulations, {name}!')


def get_correct_answer(number1: int, number2: int, operator: str) -> int:
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    else:
        return number1 * number2
