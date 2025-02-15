alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = {c: i for i, c in enumerate(alph, 1)}
ans = 0
p = 0
for c in 'FEDBED':
    ans += d[c] * 26**p
    p += 1
print(ans)