from brain_games import engine

from typing import Tuple

from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_GEN_LOW = 2
RANDOM_GEN_HIGH = 100


def play_prime_game():
    name = engine.greet_and_get_name()
    engine.run_game(RULES, name, get_question_and_answer())


def get_question_and_answer() -> Tuple[str, str]:
    question_number = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question = f'Question: {question_number}'
    answer = 'yes' if is_prime(question_number) else 'no'
    return (question, answer)


def is_prime(number: int) -> bool:
    divider = number // 2
    while divider > 1:
        if number % divider == 0:
            return False
        divider -= 1
    return True