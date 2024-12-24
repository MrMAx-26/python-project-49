#!/usr/bin/env python

from brain_games.games.gcd_game import RULES, get_question_and_answer
from brain_games.engine import run_game, greet_and_get_name


def main():
    run_game(RULES, greet_and_get_name(), get_question_and_answer)


if __name__ == '__main__':
    main()