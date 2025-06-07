with open('zadacha-26-39c287e8-9052-4900-9c2b-0c972182cce2.txt') as f:
    n = int(f.readline())
    students = []

    for _ in range(n):
        parts = f.readline().split()
        sid = int(parts[0])
        grades = list(map(int, parts[1:]))
        twos = grades.count(2)
        avg = sum(grades) / 4
        students.append((sid, grades, twos, avg))

# Разделяем
passed = [(sid, avg) for sid, grades, twos, avg in students if twos == 0]
failed = [(sid, twos) for sid, grades, twos, avg in students if twos > 0]

# Сортируем
passed.sort(key=lambda x: (-x[1], x[0]))
failed.sort(key=lambda x: (x[1], x[0]))

# Собираем итоговый список ID
ranking = [sid for sid, _ in passed] + [sid for sid, _ in failed]

# Ищем границу 25%
top_25_count = n // 4
stipend_ids = ranking[:top_25_count]

# Среди них ищем последний ID стипендиата (в passed уже гарантировано без двоек)
last_stipend_id = None
for sid in reversed(stipend_ids):
    if any(sid == s[0] for s in passed):
        last_stipend_id = sid
        break

# Ищем первого с более чем двумя двойками
bad_id = None
for sid, grades, twos, avg in students:
    if twos > 2:
        # Где он в финальном рейтинге
        if sid in ranking:
            bad_index = ranking.index(sid)
            if bad_id is None or bad_index < ranking.index(bad_id):
                bad_id = sid

print(last_stipend_id, bad_id)
print(passed)
print(failed)