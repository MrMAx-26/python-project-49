#!/usr/bin/env python


def main():
    from random import randint

    from prompt import string

    from brain_games import cli
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question = randint(0, 100)
        correct_answer = 'yes' if is_even(question) else 'no'
        print(f'Question: {question}')
        answer = string('Your answer: ')
        if correct_answer == answer:
            print('Correct!')
            i += 1
        else:
            i = 4
    if i == 4:
        print(f"'{answer}' is wrong answer ;(. Correct answer was " + 
            f"'{correct_answer}'.")
        print(f"Let's try again, {name}!")
    if i == 3:
        print(f'Congratulations, {name}!')


def is_even(question: int) -> bool:
    return True if question % 2 == 0 else False


if __name__ == '__main__':
    main()