def greet_and_get_name():
    from brain_games import cli
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name