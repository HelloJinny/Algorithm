# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다.
A, B = input().split()

# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다.
A = int(A[::-1])
B = int(B[::-1])

# 첫째 줄에 상수의 대답을 출력한다.
if A > B:
    print(A)
else:
    print(B)