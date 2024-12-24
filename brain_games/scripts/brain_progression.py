#!/usr/bin/env python

from brain_games.engine import greet_and_get_name, run_game
from brain_games.games.progression_game import RULES, get_question_and_answer


def main():
    run_game(RULES, greet_and_get_name(), get_question_and_answer)


if __name__ == '__main__':
    main()