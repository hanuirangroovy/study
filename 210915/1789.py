
n = int(input())
num = 0
while num*(num+1) / 2 <= n:
    num += 1
print(num-1)


#
# if n % 2 == 0  # 입력값이 짝수일때는 홀수숫자까지
#
# else:   # 입력값이 홀수일때는 짝수숫자까지