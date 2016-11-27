import random

def generator(n, even):
    if n == 0:
        if even:
            return ""
        else:
            return str(random.randrange(2))

    sides = str(random.randrange(2))
    return (sides + generator(n-1, even) + sides)


def convert_length(length):
    length = int(length / 2)
    if (length % 2) == 0:
        return [length, True]
    else:
        return [length, False]
