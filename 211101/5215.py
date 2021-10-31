import sys
sys.stdin = open("input_5215.txt","r")

t = int(input())
for tc in range(1,t+1):
    n, l = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    g_s = [] #맛에 대한 점수
    g_c = [] #칼로리
    maxV = 0
    for i in range(1<<n):
        for j in range(n+1):
            if i & (1<<j):
                g_s.append(g[j][0])
                g_c.append(g[j][1])
                if sum(g_c) <= l:
                    maxG = sum(g_s)
                    if maxG >= maxV:
                        maxV = maxG
                        g_s = []
                        g_c = []

    print('#{} {}'.format(tc, maxV))