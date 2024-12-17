def play_progression_game():
    from prompt import string

    from brain_games import engine

    name = engine.greet_and_get_name()
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        progression = engine.hide_element_and_get_correct_answer(
            engine.generate_progression())
        question = progression[0]
        print('Question: ' + " ".join([str(i) for i in question]))
        answer = int(string('Your answer: '))
        correct_answer = progression[1]
        i = engine.check_answer(answer, correct_answer, i)
    engine.print_result_of_game(answer, correct_answer, name, i)