def play_prime_game():
    from random import randint

    from prompt import string

    from brain_games import engine

    MAX_NUMBER = 100
    MIN_NUMBER = 2

    name = engine.greet_and_get_name()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        question = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = 'yes' if engine.is_prime(question) else 'no'
        print(f'Question: {question}')
        answer = string('Your answer: ')
        i = engine.check_answer(answer, correct_answer, i)
    engine.print_result_of_game(answer, correct_answer, name, i)