# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
T = int(input())

for _ in range(T):
    alphabet = str(input())
    # 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.
    print(alphabet[0] + alphabet[-1])