import sys
sys.stdin = open(f'input_1946.txt','r')

# 합친 후 10 줄씩 자르기
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = []
    for _ in range(n):
        a, b = input().split()
        lst.append(a*int(b))
        addlst = "".join(lst)

    print('#{}'.format(tc))
    for i in range(0, len(addlst), 10):
        print(addlst[i:i + 10])



