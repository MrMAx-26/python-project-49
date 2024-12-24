from typing import Callable, Tuple, TypeAlias

from prompt import string

ROUNDS = 3
GameLogicFunction: TypeAlias = Callable[[], Tuple[str, str]]


def greet_and_get_name():
    from brain_games import cli

    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name 


def run_game(rules, name, get_question_and_answer: GameLogicFunction):
    print(rules)
    for _ in range(ROUNDS):
        question, correct_answer = get_question_and_answer()
        print(question)
        answer = string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was " + 
            f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')