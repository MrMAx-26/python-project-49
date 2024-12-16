def welcome_user():
    from prompt import string

    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
    
    


