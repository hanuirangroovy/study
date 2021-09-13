import sys
sys.stdin = open(f'input_5603.txt','r')

for tc in range(int(input())):
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    sum_lst = 0
    sum_lst = sum(lst)
    avg_lst = sum_lst / len(lst)
    result_lst = []
    for j in range(n):
        if lst[j] > avg_lst:
            result_lst.append(abs(lst[j] - avg_lst))
            result_sum = sum(result_lst)
            result = round(result_sum)
    print('#{} {}'.format(tc+1, result))
