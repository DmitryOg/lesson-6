def is_very_long(password):
    result = len(password) >= 12
    return result

def has_digit(password):
    found_digit = any(i.isdigit() for i in password)
    return found_digit

def has_upper_letters(password):
    found_upper_letters = any(i.isupper() for i in password)
    return found_upper_letters

def has_lower_letters(password):
    found_lower_letters = any(i.islower() for i in password)
    return found_lower_letters

def has_symbols(password):
    found_symbols = any(not i.isdigit() and not i.isalpha() for i in password)
    return found_symbols


def main():
    password = input('Введите пароль:')
    score = 0
    functions = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password)
    ]

    for i in functions:
        if i:
            score += 2


    print('Рейтинг пароля:', score)
if __name__ == "__main__": 
    main()


























