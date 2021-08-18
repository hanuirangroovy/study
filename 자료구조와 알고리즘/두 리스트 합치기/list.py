import sys
for i in range(1, 6):
    sys.stdin=open(f'in{i}.txt', "r")

def sort(list):
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return list

N = int(input())
lst_1 = list(map(int, input().split()))
M = int(input())
lst_2 = list(map(int, input().split()))

lst = lst_1 + lst_2
result = sort(lst)

for k in result:
    print(k, end=' ')


