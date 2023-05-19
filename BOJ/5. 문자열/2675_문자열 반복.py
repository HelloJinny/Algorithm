# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
T = int(input())

for _ in range(T):
    # 각 테스트 케이스는 반복 횟수 R, 문자열 S가 공백으로 구분되어 주어진다.
    R, S = input().split()
    R = int(R)

    # 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
    for i in S:
        P = R * i
        # 각 테스트 케이스에 대해 P를 출력한다.
        print(P, end='', sep='')
    print()