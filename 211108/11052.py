import sys
sys.stdin = open("input_11052.txt","r")

n = int(input())
lst = list(map(int, input().split()))
num = len(lst)
for i in range(1,len(lst)+1):
