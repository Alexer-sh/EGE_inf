from itertools import product
count = 0
for x in product('ПЕТЯ', repeat=6):
    slovo = ''.join(x)
    if all(pair not in slovo for pair in 'ПП ПТ ТП ТТ ЕЯ ЯЕ ЕЕ ЯЯ'.split()):
        count += 1
print(count)