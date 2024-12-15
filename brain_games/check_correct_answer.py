def check_answer(answer, correct_answer, i) -> int:
    if answer == correct_answer:
        print('Correct!')
        return i + 1
    else:
        i = 4
        return i