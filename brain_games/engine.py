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
