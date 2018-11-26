import sys


def get_list_segment(l, number, offset):
    return [x for x in l if x < number + offset]


def get_total_difference(l, guesses):
    return sum(min(abs(x - number) for x in guesses) for number in l)


def make_guess(l):
    guesses = []
    guess = l[0]
    offset = 100
    old_diff = sys.maxsize
    segment = get_list_segment(l, guess, offset)
    while len(guesses) < 10:
        diff = get_total_difference(segment, guesses + [guess])
        if diff <= old_diff:
            old_diff = diff
            guess += 1
        else:
            guesses.append(guess - 1)
            segment = get_list_segment(l, guess, len(guesses) * offset + offset - guess)
            old_diff = sys.maxsize
    return guesses


if __name__ == '__main__':

    data = []

    with open("f3") as file:
        raw_data = file.read().strip().split()
    for number_raw in raw_data:
        nbr = int(number_raw)
        if 1 <= nbr <= 1000:
            data.append(int(number_raw))
        else:
            print("Die Datei enthaelt Zahlen die nicht zwischen 0 und 1000 liegen! Linie %d")

    data.sort()

    if len(data) <= 10:
        print("%r + %d " % (data + [0] * (10 - len(data)), len(data) * 25))
    else:
        result = make_guess(data)
        print("%r + %d " % (result, len(data) * 25 - get_total_difference(data, result)))
