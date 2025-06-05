from itertools import permutations

count = 0
alf = '0123456789'
for i in permutations(alf, 4):
    i1 = ''.join(i)
    bad_pairs = ["13", "15", "17", "19", "31", "35", "37", "39",
                 "51", "53", "57", "59", "71", "73", "75", "79",
                 "91", "93", "95", "97"]
    bad_pairs1 = ["02", "04", "06", "08", "20", "24", "26", "28",
                 "40", "42", "46", "48", "60", "62", "64", "68",
                 "80", "82", "84", "86"]
    if i[0] != '0' and not any(pair in i1 for pair in bad_pairs) and not any(pair in i1 for pair in bad_pairs1):
        count += 1
        print(i1)

print(count)
