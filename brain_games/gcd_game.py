def play_gcd_game():
    from random import randint

    from prompt import string

    from brain_games import engine

    MAX_NUMBER = 100
    MIN_NUMBER = 1

    name = engine.greet_and_get_name()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        number1, number2 = randint(MIN_NUMBER, MAX_NUMBER), randint(MIN_NUMBER, MAX_NUMBER)
        print(f'Question: {number1} {number2}')
        answer = int(string('Your answer: '))
        correct_answer = engine.get_gcd(number1, number2)
        i = engine.check_answer(answer, correct_answer, i)
    engine.print_result_of_game(answer, correct_answer, name, i)