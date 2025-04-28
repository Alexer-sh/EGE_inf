f = open("34.txt").readlines()
N = len(f)
field = [list(map(int, t.strip().split(';'))) for t in f]

dp_no_spesh = [[-1 for _ in range(N)] for _ in range(N)]
dp_spesh = [[-1 for _ in range(N)] for _ in range(N)]

# Начальная зарядка
start_charge = field[N-1][0]
start_charge = min(100, max(0, start_charge))
if start_charge != 0:
    dp_no_spesh[N-1][0] = start_charge
dp_spesh[N-1][0] = start_charge

for i in range(N-1, -1, -1):
    for j in range(N):
        for di, dj in [(-1, 0), (0, 1)]:  # Вверх или вправо
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                # Новое изменение заряда
                for dp, allow_zero in [(dp_no_spesh, False), (dp_spesh, True)]:
                    if dp[i][j] != -1:
                        new_charge = dp[i][j] + field[ni][nj]
                        new_charge = min(100, max(0, new_charge))
                        if new_charge == 0 and not allow_zero:
                            continue  # Нельзя спешиваться
                        if new_charge > dp[ni][nj]:
                            dp[ni][nj] = new_charge

# Вывод ответа
print(dp_no_spesh[0][N-1], dp_spesh[0][N-1])
