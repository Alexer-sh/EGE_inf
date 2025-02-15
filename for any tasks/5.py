from itertools import permutations, product


def count_valid_numbers():
    digits = list(range(12))  # Доступные цифры (0-11)
    even_digits = {0, 2, 4, 6, 8, 10}  # Четные цифры (4 включаем отдельно)
    odd_digits = {1, 3, 5, 7, 9, 11}  # Нечетные цифры
    count = 0

    for positions in permutations(range(5), 2):  # Выбираем 2 позиции для цифры 4
        for values in product(digits, repeat=5):  # Перебираем все возможные числа
            num = list(values)
            if num[0] == 0:
                continue  # Число не может начинаться с 0

            if num[positions[0]] != 4 or num[positions[1]] != 4:
                continue  # Две цифры 4 должны быть в числе

            if num.count(4) != 2:
                continue  # Должно быть ровно две 4

            valid = True
            for i in range(5):
                if num[i] == 4:
                    if i > 0 and num[i - 1] in odd_digits:
                        valid = False
                        break
                    if i < 4 and num[i + 1] in odd_digits:
                        valid = False
                        break

            if valid:
                count += 1

    return count


print(count_valid_numbers())
