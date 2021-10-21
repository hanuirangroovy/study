import sys
sys.stdin = open("input_2806.txt","r")
#N-Queen

def nqueens(col,i):  #i=depth
    global cnt
    n = len(col)-1
    if (selection(col,i)):
        lst = []
        if i==n: #끝까지 왔을 때
            lst.append(col[1:n + 1])
            cnt = len(lst)


        else:
            for j in range(1, n+1):
                col[i+1] = j
                nqueens(col,i+1)


def selection(col,i):
    k = 1
    flag = True
    while k<i and flag:
        # 같은 열에 있느냐 or 같은 대각선에 있느냐
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            flag = False
        k += 1
    return flag

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cnt = 0
    col = [0]*(n+1)
    nqueens(col, 0)

    print('#{} {}'.format(tc,cnt))
