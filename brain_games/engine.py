def greet_and_get_name():
    from brain_games import cli
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


def check_answer(answer, correct_answer, i) -> int:
    if answer == correct_answer:
        print('Correct!')
        return i + 1
    else:
        i = 4
        return i