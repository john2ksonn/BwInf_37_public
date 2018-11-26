# returns the sum of the difference from each number to the nearest guess
import random
import math


def get_summ(guesses):
    return sum(min(abs(number - guess) for guess in guesses) for number in numbers)


def guessing_2():
    result = []
    while len(result) < 10:
        result.append(
            numbers[min(enumerate([get_summ([*result, *[number]]) for number in numbers]), key=lambda x: x[1])[0]])
    return result


def guessing():
    result = []
    list_len = int(math.ceil(len(numbers) / 10))  # Runde die Nummer
    while len(result) < 10:
        segment = numbers[list_len * len(result):list_len + list_len * len(result)]
        result.append(
            min([number for number in segment],
                key=lambda number: sum(min(abs(x - guess) for guess in result + [number]) for x in segment)))
    return result


def print_biggest_diff():
    max_diff = []
    liste = numbers
    while len(max_diff) < 9:
        diff = []
        for idx in range(0, len(liste) - 1):
            diff.append(liste[idx + 1] - liste[idx])
        for idx, difference in enumerate(diff):
            if difference in max_diff:
                diff[idx] = 0
        max_value = [max(diff), []]
        for idx, value in enumerate(diff):
            if value == max_value[0]:
                max_value[1].append(idx)
        while len(max_value[1]) + len(max_diff) > 9:
            del max_value[1][random.randint(0, len(max_value[1]) - 1)]
        max_diff.extend(max_value[1])
    print(max_value)
    max_diff = [0] + max_diff + [len(numbers) - 1]
    print(max_diff)
    result = []
    for idx in range(0, len(max_diff) - 1):
        result.append()
    return result


file_name = "f2"
numbers = sorted([int(line) for line in open(file_name).readlines() if 1 <= int(line) <= 1000])
resulting = sorted(guessing())
print("Zahlen %r\nEinnahmen: %d€ - Ausgaben: %d€ = Gewinn: %d€" % (
    resulting, len(numbers) * 25, get_summ(resulting), len(numbers) * 25 - get_summ(resulting)))

if file_name == "f1":
    resulting = [55, 150, 250, 350, 450, 550, 650, 750, 850, 950]
elif file_name == "f2":
    resulting = [59, 170, 229, 367, 426, 540, 676, 763, 862, 929]
else:
    resulting = [80, 160, 240, 340, 440, 540, 640, 720, 840, 920]

print("Zahlen %r\nEinnahmen: %d€ - Ausgaben: %d€ = Gewinn: %d€" % (
    resulting, len(numbers) * 25, get_summ(resulting), len(numbers) * 25 - get_summ(resulting)))

resulting = sorted(guessing_2())
print("Zahlen %r\nEinnahmen: %d€ - Ausgaben: %d€ = Gewinn: %d€" % (
    resulting, len(numbers) * 25, get_summ(resulting), len(numbers) * 25 - get_summ(resulting)))
