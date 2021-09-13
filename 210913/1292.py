start, end = map(int, input().split())
lst = []
for i in range(1, 47):
    lst += [i] * i
    lst_slice = lst[start-1:end]
sum = 0
for j in lst_slice:
     sum += int(j)
print(sum)

