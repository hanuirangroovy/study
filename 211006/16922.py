n = int(input())
lst = []
for i in range(n+1): # 1의 개수
    for j in range(n+1-i): # 5의 개수
        for k in range(n+1-i-j): # 10의 개수
            fif = n-i-j-k   #50의 개수
            result = i + 5*j + 10*k + 50*fif
            lst.append(result)
print(len(lst))