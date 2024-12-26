#!/usr/bin/env python

from brain_games.engine import run_game
from brain_games.games.progression_game import RULES, get_question_and_answer


def main():
    run_game(RULES, get_question_and_answer)


if __name__ == '__main__':
    main()