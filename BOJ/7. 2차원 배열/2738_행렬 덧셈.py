# N*M 크기의 두 행렬 A와 B
A, B = [], []

# 첫째 줄에 행렬의 크기 N 과 M이 주어진다.
N, M = map(int, input().split())

# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
for row in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다.
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()