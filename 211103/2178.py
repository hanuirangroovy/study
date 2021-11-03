import sys
sys.stdin = open("input_3584","r")

def find_p(a, b, data):
    i = 0
    f = []
    while i < len(data):
        if data[i + 1] == a:
            f.append(data[i])
            a = data[i]
            i = 0
        else:
            i = i + 2

    i = 0
    while i < len(data):
        if data[i + 1] == b:
            if data[i] in f:
                return data[i]
            b = data[i]
            i = 0
        else:
            i = i + 2


def count_n(x, data):
    i = 0
    son = []
    n = 1
    while 1:
        while i < len(data):
            if data[i] == x:
                son.append(data[i + 1])
                n += 1
            i = i + 2
        if len(son) != 0:
            x = son.pop()
            i = 0
        else:
            break
    return n


T = int(input())
for test_case in range(1, T + 1):
    V, E, a, b = map(int, input().split())
    data = [0 for i in range(E * 2)]
    data = list(map(int, input().split()))
    x = find_p(a, b, data)
    n = count_n(x, data)
    print('#{} {} {}'.format(test_case, x, n))