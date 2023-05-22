# 총 다섯줄의 입력이 주어진다.
words = [input() for i in range(5)]

# 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다.
# 다음에 두 번째 글자들을 세로로 읽는다.
# 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
# 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            # 영석이가 세로로 읽은 순서대로 글자들을 출력한다.
            print(words[j][i], end='')