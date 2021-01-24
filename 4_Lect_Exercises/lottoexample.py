# Program to demonstrate lists and sets

from random import choice

lottonumbers = list()
number_select = list(range(1,48))

while len(lottonumbers) < 6:
    y = choice(number_select)

    if y not in lottonumbers:
        lottonumbers.append(y)
        number_select.remove(y)


print(lottonumbers)


# Example 2
from random import shuffle
quick_pick = []

lottonumbers.clear()
lottonumbers = list(range(1,49))

shuffle(lottonumbers)

quick_pick.extend(lottonumbers[:6])

quick_pick.sort()
print(quick_pick)