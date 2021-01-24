# Program to calculate the Mode of a Dictionary -> Created by Andy Blankley


def calc_mode2(numbers):

    values = sorted(list(set(numbers)))

    freq = [numbers.count(value) for value in values]

    index = freq.index(max(freq))
    return values[index]



