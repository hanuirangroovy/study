import sys
sys.stdin = open(f'input_5603.txt','r')

for tc in range(int(input())):
    n = int(input())
    lst = [int(input()) for _ in range(n)]
    sum_lst = 0
    for i in lst:
        sum_lst += i
        avg_lst = sum_lst / len(lst)
        result_lst = []
        for j in range(n):
            result_lst.append(abs(lst[j] - avg_lst))
            result_sum = 0
            for k in range(len(result_lst)):
                result_sum += result_lst[k]
                result = round(result_sum/2)
print('#{} {}'.format(tc+1, result))
