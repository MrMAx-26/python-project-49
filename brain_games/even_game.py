def play_even_game():
    from random import randint

    from prompt import string

    from brain_games import engine

    name = engine.greet_and_get_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question = randint(0, 100)
        correct_answer = 'yes' if engine.is_even(question) else 'no'
        print(f'Question: {question}')
        answer = string('Your answer: ')
        i = engine.check_answer(answer, correct_answer, i)
    engine.print_result_of_game(answer, correct_answer, name, i)