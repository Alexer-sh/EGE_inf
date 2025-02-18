from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)


@lru_cache(None)
def func(x, lme, skip=(0,)):
    if x == lme:
        return 1
    if x > lme or x in skip:
        return 0
    return func(x + 1, lme, skip) + func(x * 2, lme, skip) + func(x + 5, lme, skip)


skips = (10,)
print(func(1, 8, skips) * func(8, 96, skips))