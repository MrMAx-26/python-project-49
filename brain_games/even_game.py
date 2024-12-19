def play_even_game():
    from brain_games import engine

    name = engine.greet_and_get_name()
    question_text = 'Answer "yes" if the number is even, otherwise answer "no".'
    print(question_text)
    engine.run_game(question_text, name)