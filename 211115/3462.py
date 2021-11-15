import sys
sys.stdin = open("input_3462.txt","r")

prime_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

t = int(input())
for tc in range(1,t+1):
    a, b = map(int,input().split())
    lst_a = [[0]*(i+1) for i in range(31)]
    lst_b = [[0]*(i+1) for i in range(31)]
    lst_a[0][0] = 1
    lst_b[0][0] = 1
    for i in range(30):
        for j in range(i+1):
            lst_a[i+1][j] += lst_a[i][j]*(100-a)*0.01
            lst_a[i+1][j+1] += lst_a[i][j]*a*0.01
            lst_b[i+1][j] += lst_b[i][j]*(100-b)*0.01
            lst_b[i+1][j+1] += lst_b[i][j]*b*0.01
    result_a = 0
    result_b = 0
    for i in prime_number:
        result_a += lst_a[30][i]
        result_b += lst_b[30][i]
    result = round(1-(1-result_a)*(1-result_b),5)
    print('#%d %.5f' %(tc, result))


