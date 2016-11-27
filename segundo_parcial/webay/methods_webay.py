def string_handler(string):
    state = 1
    for x in string:
        temp = x
        temp = temp.lower()
        state = automata(temp, state)

    print(state)
    if state == 8 or state == 4:
        print("de lujo", state)


def automata(symbol, state):
    if state == 1:
        return state_one(symbol)
    elif state == 2:
        return state_two(symbol)
    elif state == 3:
        return state_three(symbol)
    elif state == 4:
        return state_four(symbol)
    elif state == 5:
        return state_five(symbol)
    elif state == 6:
        return state_six(symbol)
    elif state == 7:
        return state_seven(symbol)
    elif state == 8:
        return state_eight(symbol)
    else:
        return -1


def state_one(symbol):
    if symbol == 'e':
        return 5
    elif symbol == 'w':
        return 2
    else:
        return 1


def state_two(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 3
    else:
        return 1


def state_three(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    elif symbol == 'b':
        return 4
    else:
        return 1


def state_four(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    elif symbol == 'a':
        return 7
    else:
        return 1


def state_five(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    elif symbol == 'b':
        return 6
    else:
        return 1


def state_six(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    elif symbol == 'a':
        return 7
    else:
        return 1


def state_seven(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    elif symbol == 'y':
        return 8
    else:
        return 1


def state_eight(symbol):
    if symbol == 'w':
        return 2
    elif symbol == 'e':
        return 5
    else:
        return 1
