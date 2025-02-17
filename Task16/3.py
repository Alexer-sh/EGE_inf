F = [0]*15
G = [0]*15
F[1] = G[1] = 1
for i in range(2,15):
    F[i] = 2*F[i-1] + G[i-1] - 2*i
    G[i] = F[i-1] + 2*G[i-1] + i
print(F[14] + G[14])