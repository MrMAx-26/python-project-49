def play_gcd_game():
    from brain_games import engine

    name = engine.greet_and_get_name()
    question_text = 'Find the greatest common divisor of given numbers.'
    print(question_text)
    engine.run_game(question_text, name, tyoe_answer='int')