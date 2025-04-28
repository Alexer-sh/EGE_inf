f = open("12468.txt").readlines()
N = len(f)
dp = [[0 for _ in range(N)] for _ in range(N)]
cnt = [[0 for _ in range(N)] for _ in range(N)]
coins = [[0 for _ in range(N)] for _ in range(N)]

m = 0
for t in f:
    coins[m] = list(map(int, t.strip().split(';')))
    m += 1

for i in range(N-1, -1, -1):
    for j in range(N):
        if i == N-1 and j == 0:
            dp[i][j] = coins[i][j]
            cnt[i][j] = 1
        else:
            max_val = -1
            ways = 0
            if i+1 < N:  # снизу (мы пришли СНИЗУ = двигались ВВЕРХ)
                if dp[i+1][j] > max_val:
                    max_val = dp[i+1][j]
                    ways = cnt[i+1][j]
                elif dp[i+1][j] == max_val:
                    ways += cnt[i+1][j]
            if j-1 >= 0:  # слева (мы пришли СЛЕВА = двигались ВПРАВО)
                if dp[i][j-1] > max_val:
                    max_val = dp[i][j-1]
                    ways = cnt[i][j-1]
                elif dp[i][j-1] == max_val:
                    ways += cnt[i][j-1]
            if max_val != -1:
                dp[i][j] = max_val + coins[i][j]
                cnt[i][j] = ways

print(dp[0][N-1], cnt[0][N-1])
