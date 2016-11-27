def string_handler(string):
    string = list(string)
    auxilliar_result = []
    state = 0
    moving = 0
    while True:
        try:
            if moving < 0:
                raise Exception

            auxilliar_result = turing_machine_handler(state, string[moving])
            string[moving] = auxilliar_result[1]
        except Exception as e:
            auxilliar_result = turing_machine_handler(state, 'B')

        state = auxilliar_result[0]
        moving = moving + auxilliar_result[2]

        if state == -1 or state == 4:
            break

    return state

def turing_machine_handler(state, symbol):
    if state == 0:
        return state0(symbol)
    elif state == 1:
        return state1(symbol)
    elif state == 2:
        return state2(symbol)
    elif state == 3:
        return state3(symbol)
    elif state == 4:
        return state4(symbol)


def state0(symbol):
    if symbol == '0':
        return [1, 'X', 1]
    elif symbol == 'Y':
        return [3, 'Y', 1]
    else:
        return [-1, '', 0]

def state1(symbol):
    if symbol == '0':
        return [1, '0', 1]
    elif symbol == '1':
        return [2, 'Y', -1]
    elif symbol == 'Y':
        return [1, 'Y', 1]
    else:
        return [-1, '', 0]

def state2(symbol):
    if symbol == '0':
        return [2, '0', -1]
    elif symbol == 'X':
        return [0, 'X', 1]
    elif symbol == 'Y':
        return [2, 'Y', -1]
    else:
        return [-1, '', 0]

def state3(symbol):
    if symbol == 'Y':
        return [3, 'Y', 1]
    elif symbol == 'B':
        return [4, 'B', 1]
    else:
        return [-1, '', 0]

def state4(symbol):
    return [4, 'B', 0]
