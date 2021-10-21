# 백준 1120 문자열
# adaabc aababbc
a, b = input().split()
result = []
#앞에서부터 이동시키며 최대한 맞는 곳 찾기
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    result.append(cnt)
print(min(result))