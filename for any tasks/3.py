f = open("18.txt")
a = f.readlines()
f.close()
b = []
for t in a:
    row = list(map(int, t.strip().split()))
    b.append(row)
print(b)

