from brain_games import engine

from typing import Tuple

from random import randint, choice

RULES = 'What is the result of the expression?'
RANDOM_GEN_LOW = 0
RANDOM_GEN_HIGH = 25
OPERATORS = ['+', '-', '*']


def get_question_and_answer() -> Tuple[str, str]:
    question_number_first = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question_number_second = randint(RANDOM_GEN_LOW, RANDOM_GEN_HIGH)
    question_operator = choice(OPERATORS)
    question = f'Question: {question_number_first} {question_operator} {question_number_second}'
    answer = get_correct_math_answer(question_number_first, question_number_second, question_operator)
    return (question, answer)


def get_correct_math_answer(number1: int, number2: int, operator: str):
    if operator == '+':
        return str(number1 + number2)
    elif operator == '-':
        return str(number1 - number2)
    else:
        return str(number1 * number2)