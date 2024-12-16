def play_calc_game():
    from random import choice, randint

    from prompt import string

    from brain_games import engine

    name = engine.greet_and_get_name()
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        operator = choice(operators)
        number1, number2 = randint(0, 25), randint(0, 25)
        print(f'Question: {number1} {operator} {number2}')
        answer = int(string("Your answer: "))
        correct_answer = engine.get_correct_math_answer(number1, number2, operator)
        i = engine.check_answer(answer, correct_answer, i)
    engine.print_result_of_game(answer, correct_answer, name, i)