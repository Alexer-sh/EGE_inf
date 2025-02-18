def f(x, end):
    if x > end: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x + 3, end)
print(f(2, 15))
#можно ещё так, но это уже не моя идея
