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
    

def get_gcd(number1: int, number2: int) -> int:
    if number2 > number1:
        number1, number2 = number2, number1
    remainder = number2
    while remainder != 0:
        remainder = number1 % number2
        number1 = number2
        if remainder != 0:
            number2 = remainder 
    return number2