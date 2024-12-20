def greet_and_get_name():
    from brain_games import cli

    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


def check_answer(answer, correct_answer, i) -> int:
    if answer == correct_answer:
        print('Correct!')
        return i + 1
    else:
        i = 4
        return i
    

def get_gcd(number1: int, number2: int) -> int:
    if number2 > number1:
        number1, number2 = number2, number1
    remainder = number2
    while remainder != 0:
        remainder = number1 % number2
        number1 = number2
        if remainder != 0:
            number2 = remainder 
    return number2


def is_even(question: int) -> bool:
    return True if question % 2 == 0 else False


def get_correct_math_answer(number1: int, number2: int, operator: str) -> int:
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    else:
        return number1 * number2
    

def print_result_of_game(answer, correct_answer, name: str, i: int):
    if i == 4:
        print(f"'{answer}' is wrong answer ;(. Correct answer was " + 
            f"'{correct_answer}'.")
        print(f"Let's try again, {name}!")
    if i == 3:
        print(f'Congratulations, {name}!')


def generate_progression() -> list:
    from random import randint

    PROGRESSION_LEN = 10
    MAX_D = 10
    MIN_D = 1
    MAX_NUMBER = 20
    MIN_NUMBER = 0

    progression = []
    progression.append(randint(MIN_NUMBER, MAX_NUMBER))
    d = randint(MIN_D, MAX_D)
    for i in range(PROGRESSION_LEN - 1):
        progression.append(progression[i] + d)
    return progression


def hide_element_and_get_correct_answer(progression: list) -> list:
    from random import randint
    
    result = []
    element_index = randint(0, len(progression) - 1)
    correct_answer = progression[element_index]
    progression[element_index] = '..'
    result.append(progression)
    result.append(correct_answer)
    return result


def is_prime(number: int) -> bool:
    divider = number // 2
    while divider > 1:
        if number % divider == 0:
            return False
        divider -= 1
    return True


def get_question(question_text: str) -> str:
    from random import choice, randint

    OPERATORS = ('+', '-', '*')

    if question_text == ('Answer "yes" if the number is even, '
        + 'otherwise answer "no".'):
        question = randint(0, 100)
        print(f'Question: {question}')
        correct_answer = 'yes' if is_even(question) else 'no'
    elif question_text == 'What is the result of the expression?':
        operator = choice(OPERATORS)
        number1, number2 = randint(0, 25), randint(0, 25)
        print(f'Question: {number1} {operator} {number2}')
        correct_answer = get_correct_math_answer(number1, number2, operator)
    elif question_text == 'Find the greatest common divisor of given numbers.':
        number1, number2 = randint(1, 100), randint(1, 100)
        print(f'Question: {number1} {number2}')
        correct_answer = get_gcd(number1, number2)
    elif question_text == ('Answer "yes" if given number is prime. '
        + 'Otherwise answer "no".'):
        question = randint(2, 100)
        print(f'Question: {question}')
        correct_answer = 'yes' if is_prime(question) else 'no'
    elif 'What number is missing in the progression?':
        progression = hide_element_and_get_correct_answer(
            generate_progression())
        question = progression[0]
        print('Question: ' + " ".join([str(i) for i in question]))
        correct_answer = progression[1]
    return correct_answer


def run_game(question_text, name, tyoe_answer='str'): 
    from prompt import string

    i = 0
    while i < 3:
        correct_answer = get_question(question_text)
        answer = string('Your answer: ') if tyoe_answer == 'str' else int(
            string('Your answer: '))
        i = check_answer(answer, correct_answer, i)
    print_result_of_game(answer, correct_answer, name, i)