import sys
for i in range(1, 6):
    sys.stdin=open(f'in{i}.txt', "r")

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
maxV = []
# 행
for i in range(N):
    sumV = 0
    for j in range(N):
        sumV += lst[i][j]
    maxV.append(sumV)

# 열
for i in range(N):
    sumV = 0
    for j in range(N):
        sumV += lst[j][i]
    maxV.append(sumV)

#왼 대각선
sumV = 0
for i in range(N):
    sumV += lst[i][i]
maxV.append(sumV)

#오 대각선
sumV = 0
for i in range(N):
    sumV += lst[i][N-1-i]
maxV.append(sumV)

# 가장 큰 값
result = 0
for i in range(len(maxV)):
    if result < maxV[i]:
        result = maxV[i]

print(result)