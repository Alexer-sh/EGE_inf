f = open('zadanie_24.5.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'X' and k%3 == 0) or (f[i] == 'Y' and k%3 == 1) or (f[i] == 'Z' and k%3 == 2):
        #Тут мы тупо смотрим на какой именно символ из 3 попали
        k += 1
        m = max(m, k)
    elif f[i] == 'X': k = 1
    else: k = 0
print(m)