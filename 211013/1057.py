# 백준 1057 토너먼트

# 1라운드 끝날때마다 반토막

n, a, b = map(int, input().split())
cnt = 0

while a != b :
    a -= a // 2
    b -= b //2
    cnt += 1

print(cnt)

