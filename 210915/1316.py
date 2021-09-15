#백준 1316 그룹 단어 체커

n = int(input())
result = 0
for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:    # 연속해서 같은 글자가 아닐때
            if word[i] in word[i+1:]:     # 남은 쪽에 같은 글자가 있다면
                break

    else:
        result += 1

print(result)