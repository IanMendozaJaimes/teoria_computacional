def get_numbers(n):
    numbers = {}

    c0 = 0
    c1 = 0
    c2 = 0


    while True:
        c1 = n - c0

        while True:
            numbers[str(c0)+str(c1)+str(c2)] = [c0, c1, c2]

            c1 = c1 - 1
            c2 = c2 + 1

            if c1 < 0:
                break

        c0 = c0 + 1
        c2 = 0

        if c0 == n+1:
            break

    return numbers
