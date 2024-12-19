def play_progression_game():
    from brain_games import engine

    name = engine.greet_and_get_name()
    question_text = 'What number is missing in the progression?'
    print(question_text)
    engine.run_game(question_text, name, tyoe_answer='int')