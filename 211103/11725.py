from collections import deque

#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx < 0 or newx >= n or newy <0 or newy >= m:
                continue
            if g[newx][newy] == 0:
                continue
            if g[newx][newy] == 1:
                g[newx][newy] = g[x][y] + 1
                queue.append((newx,newy))
    return g[n-1][m-1]

n,m = map(int, input().split())
g = []
for _ in range(n):
    g.append(list(map(int,input())))

print(bfs(0,0))
