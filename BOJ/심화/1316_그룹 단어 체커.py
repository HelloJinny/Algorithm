# 첫째 줄에 단어의 개수 N이 들어온다.
N = int(input())

# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
group_word = N

for _ in range(N):
    word = input()

    for i in range(len(word)-1):
        # 그룹 단어인 경우
        if word[i] == word[i+1]:
            continue
        # 그룹 단어가 아닌 경우
        elif word[i] in word[i+1:]:
            group_word -= 1
            break

# 첫째 줄에 그룹 단어의 개수를 출력한다.
print(group_word)