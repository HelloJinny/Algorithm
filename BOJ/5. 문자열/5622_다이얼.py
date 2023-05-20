# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다.
alphabet = input()
dial_list = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
time = 0

# 입력한 알파벳 개수만큼 반복문 돌리기
for i in range(len(alphabet)):
    # key 탐색
    for j in dial_list.keys():
        # value 값을 time에 더한다.
        if alphabet[i] in j:
            time += dial_list[j]

# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.
print(time)
