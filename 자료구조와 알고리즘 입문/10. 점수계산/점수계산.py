# https://itcrowd2016.tistory.com/81
import sys
for i in range(1, 6):
    sys.stdin=open(f'./in{i}.txt', "r")


    n = int(input())
    lst = list(map(int,input().split()))

    score = 0
    result = 0
    for i in range(n):
        if lst[i] == 1:
            score += 1
            result += score
        else:
            score = 0    
    print(result)