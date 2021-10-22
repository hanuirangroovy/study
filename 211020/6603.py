from itertools import combinations

while True:
    lst = list(map(int, input().split()))
    n = lst[0]
    n_lst = lst[1:]
    if n == 0:
        break
    for i in combinations(n_lst,6):
        print(" ".join(map(str, i)))
    print()