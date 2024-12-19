def play_prime_game():
    from brain_games import engine

    name = engine.greet_and_get_name()
    question_text = ('Answer "yes" if given number is prime. '
        + 'Otherwise answer "no".')
    print(question_text)
    engine.run_game(question_text, name)