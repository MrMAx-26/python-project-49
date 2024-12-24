from brain_games import engine

from typing import Tuple

from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_GEN_LOW = 0
RANDOM_GEN_HIGH = 100

def play_even_game():
    name = engine.greet_and_get_name()
    engine.run_game(RULES, name, get_question_and_answer())


def get_question_and_answer() -> Tuple[str, str]:
    question_number = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question = f'Question: {question_number}'
    answer = 'yes' if is_even(question_number) else 'no'
    return (question, answer)


def is_even(question: int) -> bool:
    return question % 2 == 0