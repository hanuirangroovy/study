import sys
sys.stdin = open("input_2606.txt","r")

def dfs(s):
    global cnt
    visited[s] = 0
    for i in arr[s]:
        if visited[i]==-1:
            dfs(i)
            cnt += 1

n = int(input())   #컴퓨터수
p = int(input())  #직접 연결되어 있는 컴퓨터 쌍의 수
arr = [[]*n for _ in range(n+1)]
visited = [-1]*(n+1)
cnt = 0
for _ in range(p):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(1)
print(cnt)
