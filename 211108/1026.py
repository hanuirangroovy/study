import sys
sys.stdin = open("input_1026.txt","r")

# a 작은 값 * b 큰 값

n = int(input())
a = sorted(list(map(int,input().split())))
b = list(map(int,input().split()))
lst = []  # a*b
for i in a:
   max_b = max(b)
   result = i * max_b
   lst.append(result)
   b.remove(max_b)

print(sum(lst))