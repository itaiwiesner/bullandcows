import random


def create_code(level):
    """
    creates a code for the game depends on the level received
    :param level: the level of the game, 1 or 2 or 3
    :type level: str
    :return: a code for the game
    :rtype: str
    """
    #  level 1 code
    if level == '1':
        return ''.join([str(random.randint(1, 6)) for i in range(4)])

    # level 2 code
    if level == '2':
        return ''.join([str(random.randint(1, 8)) for i in range(8)])

    # level 3 code
    if level == '3':
        signs = ['(', ')', '*', '&', '^', '%', '$', '#', '@', '!']
        return ''.join([random.choice(signs) for i in range(10)])


def is_valid_input(user_input, code, level):
    """
    Checks if user's input is valid
    :param user_input: user's guess
    :type user_input: str
    :param code: the code the user tries to discover
    :type code: str
    :param level: game's level
    :type level: str
    :return: True or False. If the input is invalid, prints what's wrong
    :rtype: bool
    """
    # check if both input and secret_num have the length
    if len(user_input) != len(code):
        print(f"Your try's length must be {len(code)}")
        return False

    # Only if user used invalid chars!
    # Prints the valid chars depends of the level of the game.

    if level == '1':
        if len(list(filter(lambda x: x not in '123456', user_input))) != 0:
            print("Your try must include only digits between 1-4")
            return False

    if level == '2':
        if len(list(filter(lambda x: x not in '12345678', user_input))) != 0:
            print("Your try must include only digits between 1-8")
            return False

    if level == '3':
        if len(list(filter(lambda x: x not in ['(', ')', '*', '&', '^', '%', '$', '#', '@', '!'], user_input))) != 0:
            print("Your try must include these signs only '(', ')', '*', '&', '^', '%', '$', '#', '@', '!'")
            return False

    return True


def is_bull(user_try, code):
    """
    check how many bulls in user's try
    :param user_try: user's guess
    :type user_try: str
    :param code: the code the user tries to discover
    :type code: str
    :return: amount of bulls in user's try
    :rtype: int
    """
    bulls, cows = 0, 0  # bulls-בול cows-פגיעה
    for i in range(len(code)):
        if code[i] == user_try[i]:
            bulls += 1

        elif user_try[i] in code:
            cows += 1

    print(f"Bulls: {bulls}. Cows: {cows}")
    return bulls


def main():
    level = input("""Choose a level for the game: 
    level 1: 6 digits code (1-6)
    level 2: 8 digit code (1-8)
    level 3: A code made up of 10 signs '(', ')', '*', '&', '^', '%', '$', '#', '@', '!'
    """)
    # check if level is valid
    while level != '1' and level != '2' and level != '3':
        level = input("""Level must be 1 or 2 or 3. Try again: """)

    # new code for the game
    code = create_code(level)

    is_win = False
    print("Let's play Bulls & Cows")

    for i in range(12):
        user_try = input("Enter your guess: ")
        # input check
        while not is_valid_input(user_try, code, level):
            user_try = input("Try again: ")

        # check if win
        if is_bull(user_try, code) == len(code):
            print("Congratulations!!! You won")
            is_win = True
            break

    # check if lose after 4 loop is over
    if not is_win:
        print("You lost :(")


if __name__ == "__main__":
    main()
