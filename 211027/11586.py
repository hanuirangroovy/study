
n = int(input())
lst = [input() for _ in range(n)]
k = int(input())

if k == 1: #그대로
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end="")
        print()
if k == 2: #좌우반전, j만 거꾸로
    for i in range(n):
        for j in range(n-1,-1,-1):
            print(lst[i][j], end="")
        print()
if k == 3: #상하반전, i만 거꾸로
    for i in range(n-1,-1,-1):
        for j in range(n):
            print(lst[i][j], end="")
        print()
