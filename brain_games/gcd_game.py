def play_gcd_game():
    from random import randint

    from prompt import string

    from brain_games import engine

    name = engine.greet_and_get_name()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number1, number2 = randint(1, 100), randint(1, 100)
        print(f'Question: {number1} {number2}')
        answer = int(string('Your answer: '))
        correct_answer = get_gcd(number1, number2)
        i = engine.check_answer(answer, correct_answer, i)
    if i == 4:
        print(f"'{answer}' is wrong answer ;(. Correct answer was " + 
            f"'{correct_answer}'.")
        print(f"Let's try again, {name}!")
    if i == 3:
        print(f'Congratulations, {name}!')


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