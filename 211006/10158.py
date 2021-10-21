# p, q값의 경우 w,h의 1배 아래로는 그대로 1~2배 사이는 값 줄어들게. 그 이후 반복
def move(p,w):
    if p == w:
        p = w
    elif p == (2 * w):
        p = 0
    elif (p//w) % 2:
        p = w - (p % w)
    else:
        p = p % w

    return p

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

# 그냥 쭉 가기

p += t
q += t


x = move(p,w)
y = move(q,h)

print(x,y)