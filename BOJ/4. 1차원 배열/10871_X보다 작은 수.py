# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
N, X = map(int, input().split())
A = list(map(int, input().split(' ')))

# A에서 X보다 작은 수를 모두 출력한다.
for i in A:
    if X > i:
        print(i)