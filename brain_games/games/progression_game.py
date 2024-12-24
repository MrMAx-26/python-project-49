from random import randint
from typing import Tuple

from brain_games import engine

RULES = 'What number is missing in the progression?'
MIN_NUMBER = 0
MAX_NUMBER = 20
PROGRESSION_LEN = 10
MAX_D = 10
MIN_D = 1


def play_progression_game():
    name = engine.greet_and_get_name()
    engine.run_game(RULES, name, get_question_and_answer())


def get_question_and_answer() -> Tuple[str, str]:
    question_progression, answer = generate_progression_and_get_answer()
    question = 'Question: ' + ' '.join(question_progression)
    return (question, answer)


def generate_progression_and_get_answer() -> Tuple[str, list]:
    progression = []
    intermediate_number = randint(MIN_NUMBER, MAX_NUMBER)
    progression.append(str(intermediate_number))
    d = randint(MIN_D, MAX_D)
    for i in range(PROGRESSION_LEN - 1):
        intermediate_number += d
        progression.append(str(intermediate_number))
    result = []
    element_index = randint(0, len(progression) - 1)
    correct_answer = str(progression[element_index])
    progression[element_index] = '..'
    result.append(progression)
    result.append(correct_answer)
    return result