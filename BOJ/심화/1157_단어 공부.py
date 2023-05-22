# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
word = input().upper()

# 중복된 문자 값 제거
word_list = list(set(word))

# 빈 리스트 생성
cnt = []

# count 함수를 통해 입력받은 문자열 내 알파벳 개수를 빈 리스트에 입력
for i in word_list:
    count = word.count(i)
    cnt.append(count)

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])