from typing import Tuple

from random import randint

from brain_games import engine

RULES = 'Find the greatest common divisor of given numbers.'
RANDOM_GEN_LOW = 1
RANDOM_GEN_HIGH = 100


def play_gcd_game():
    name = engine.greet_and_get_name()
    engine.run_game(RULES, name, get_question_and_answer())
    
    
def get_question_and_answer() -> Tuple[str, str]:
    question_number_first = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question_number_second = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question = f'Question: {question_number_first} {question_number_second}'
    answer = get_gcd(question_number_first, question_number_second)
    return (question, answer)


def get_gcd(number1: int, number2: int) -> int:
    if number2 > number1:
        number1, number2 = number2, number1
    remainder = number2
    while remainder != 0:
        remainder = number1 % number2
        number1 = number2
        if remainder != 0:
            number2 = remainder 
    return str(number2)


