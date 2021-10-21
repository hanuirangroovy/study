# 백준 1980 햄버거 사랑

# n: 타워버거 먹는 minute , m: 불고기버거 먹는 minute, t = 주어진 minute
# cnt : 먹은 햄버거 개수, coke : 콜라마신 시간
# 3 5 55
n, m, t = map(int,input().split())

if n < m:   # 먹는데 시간 적게 걸리는 햄버거를 더 많이
    max_n = t // n
    for i in range(max_n, 0, -1):
        if (t - i * n) % m == 0:
            print(i, (t - i * n) // m)
            break
        else:             # coke 발생
            pass
            # for j in range(1,t):
            #     coke = t -j

elif m < n:
    pass
else:
    cnt = t // m
    coke = t - (cnt*m)
    print(cnt, coke)
