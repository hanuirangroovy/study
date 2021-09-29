# 백준 2839 설탕배달

w = int(input())
result = 0

max_5 = w // 5  #5로 나눌 수 있는 최대 몫
if max_5 > 0:   #5보다 같거나 클 때
    for i in range(max_5,-1,-1):   #최소개수이기에 최대몫에서부터 거꾸로

        if (w-i*5) % 3 == 0:
            a = (w-i*5) // 3
            print(i+a)
            break
        # elif w % 3 == 0:  # only 3의 배수일 때
        #     print(w//3)
        #     break
        # else:
        #     print(-1)
        #     break

else: # 5보다 작을 때
    if w % 3 == 0:
        print(w//3)
    else:
        print(-1)

