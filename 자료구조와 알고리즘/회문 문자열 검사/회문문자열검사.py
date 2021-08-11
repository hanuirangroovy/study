# https://itcrowd2016.tistory.com/81
import sys
for i in range(1, 6):
    sys.stdin=open(f'in{i}.txt', "r")

    n = int(input())
    for i in range(n):
        word = input().upper()
        if word == word[::-1]:
            print("YES")
        else:
            print("NO")


