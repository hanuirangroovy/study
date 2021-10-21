'''
7
9 9 4 1 4 9 9
7
4 4 9 1 9 4 4
3
2 5 4

57 54 10
'''
n = int(input())
lst = list(map(int, input().split()))
result = 0
a = []
a.append(lst[0])

#누적합 구하기
for i in range(1,n):
    a.append(a[i-1]+lst[i])

# 벌통 중간에 있을 때 : (n-2)까지 더한 값에 첫번째 위치 통값 빼주고 벌통 위치 값 빼주기
for i in range(1,n-2):
    result = max(result, a[n-2]-lst[0]+lst[i])
# 벌통 오른쪽에 있을 때 : 다른 벌 있는 곳(i) 뺴고 끝까지 다 먹음 + i부터 끝까지 다 먹음
for i in range(1,n-1):
    result = max(result, (a[n-1]-lst[0]-lst[i])+(a[n-1]-a[i]))
# 벌통 왼쪽에 있을 때 : 전체에서 i번째 값 뺀 값 + i번째 앞의 값 다 먹기
for i in range(1,n-1):
    result = max(result, (a[n - 2] - lst[i]) + a[i - 1])

print(result)